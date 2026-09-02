import os
import io
import json
from typing import List
from fastapi import APIRouter, HTTPException, status, Depends, UploadFile, File 
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from google import genai
from google.genai import types
from schemas import chatRequest, IngestLongDocRequest, IngestResponse, AskRequest, AskResponse
from models import Document, Chat_History
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from pypdf import PdfReader

router = APIRouter(prefix="/ai_chat", tags=["AI Chat"])

api_key = os.getenv("GEMINI_SECRET_KEY")
if not api_key:
    raise HTTPException(status_code = 500, detail="GEMINI_SECRET_KEY environment variable is not set.")
client = genai.Client(api_key=api_key)
print("🚀 Gemini Chat Session Initialized (With Memory and Personality!). Type 'exit' to quit.")

def chunk_text(text : str, chunk_size : int = 500, overlap : int = 100) -> List[str]:
    if len(text) <= chunk_size:
        return [text]
    
    chunks = []
    start = 0 
    step = chunk_size - overlap
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end].strip())
        start += step
        
    return chunks 

@router.post("/document/ingest-long", response_model = IngestResponse)
def ingest_long_document(payload : IngestLongDocRequest, db : Session = Depends(get_db)):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text content cannot be empty.")
    
    raw_chunks = chunk_text(payload.text, payload.chunk_size, payload.overlap)
    inserted = 0
    
    for chunk in raw_chunks:
        result = client.models.embed_content(
            model="gemini-embedding-2",
            contents=chunk
        )
        embeddings = result.embeddings[0].values
        
        db_doc = Document(
            content = chunk,
            embeddings = embeddings
        )
        db.add(db_doc)
        inserted += 1
        
    db.commit()
    
    return IngestResponse(
        message=f"Successfully sliced text into {inserted} overlapping chunks and indexed in pgvector.",
        inserted_count= inserted
    )
        
@router.post('/document/upload', response_model=IngestResponse)
async def upload_and_ingest_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_bytes = await file.read()
    extracted_text = ""
    
    if file.filename.endswith('.txt'):
        extracted_text += file_bytes.decode('utf-8')
    elif file.filename.endswith('.pdf'):
        try:
            pdf_reader = PdfReader(io.BytesIO(file_bytes))
            for page in pdf_reader.pages:
                extracted_text += page.extract_text() + "\n"
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error reading PDF: {str(e)}")  
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type. Only .txt and .pdf are allowed.")
    
    if not extracted_text.strip():
        raise HTTPException(status_code=400, detail="Extracted text is empty. Please check the file content.")
    
    raw_chunks = chunk_text(extracted_text, chunk_size=500, overlap=100)
    inserted = 0 
    
    for chunk in raw_chunks:
        result = client.models.embed_content(
            model="gemini-embedding-2",
            contents=chunk
        )
        embeddings = result.embeddings[0].values
        
        db_doc = Document(
            source_name=file.filename,
            content=chunk,
            embeddings=embeddings
        )
        db.add(db_doc)
        inserted += 1
        
    db.commit()
    
    return IngestResponse(
        message=f"Successfully sliced text into {inserted} overlapping chunks and indexed in pgvector.",
        inserted_count=inserted   
    )

@router.post('/rag/ask-stream')
def ask_question(payload: AskRequest, db: Session = Depends(get_db)):
    
    user_message = Chat_History(session_id=payload.session_id, role="user", content=payload.question)
    db.add(user_message)
    db.commit()
    
    past_messages = db.query(Chat_History).filter(
        Chat_History.session_id == payload.session_id
    ).order_by(Chat_History.id).all()
    
    formatted_history = []
    for msg in past_messages[:-1]:
        safe_role = "model" if msg.role == "assistant" else msg.role
        formatted_history.append(
            types.Content(
                role=safe_role,
                parts=[types.Part.from_text(text=msg.content)]
            )
        )
    
    query_result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=payload.question
    )
    query_embeddings = query_result.embeddings[0].values
    
    stmt = select(Document).order_by(
        Document.embeddings.cosine_distance(query_embeddings)
    ).limit(payload.top_k)
    
    results = db.execute(stmt).scalars().all() 
    if not results:
        raise HTTPException(status_code=404, detail="Database contains no document embeddings.")
    
    retrieved_contexts = [doc.content for doc in results]
    combined_context = "\n\n---\n\n".join(retrieved_contexts)
    
    rag_prompt = f"""
    You are a technical assistant. Answer the user's latest question using ONLY the provided Context sections.
    Context Sections:
    {combined_context}
    
    Latest User Question:
    {payload.question}
    """
    
    def generate_stream():
        chat = client.chats.create(
            model="gemini-3.6-flash",
            history=formatted_history,
            config={"system_instruction": rag_prompt}
        )
        response_stream = chat.send_message_stream(message=payload.question)
        
        initial_payload = {
            "Session ID": payload.session_id,
            "Question": payload.question,
            "Status": "Context Loaded"
        }
        yield json.dumps(initial_payload) + '\n'
        
        full_ai_response = ""
        
        for chunk in response_stream:
            if chunk.text:
                full_ai_response += chunk.text
                chunk_payload = {"Answer Chunk" : chunk.text}
                yield json.dumps(chunk_payload) + '\n'
        
        ai_message = Chat_History(session_id=payload.session_id, role="assistant", content=full_ai_response)
        db.add(ai_message)
        db.commit()
        
    return StreamingResponse(generate_stream(), media_type="application/x-ndjson")
    