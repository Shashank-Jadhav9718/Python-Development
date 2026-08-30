import os
import json
from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from google import genai
from schemas import chatRequest, IngestLongDocRequest, IngestResponse, AskRequest, AskResponse
from models import Document
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select

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
        

@router.post('/rag/ask')
def ask_question(payload: AskRequest, db: Session = Depends(get_db)):
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
    You are a technical assistant. Answer the question using ONLY the provided Context sections below.
    If the answer is not clearly present in the context, say "I do not have that information in my database."

    Context Sections:
    {combined_context}

    User Question:
    {payload.question}
    """
    def generate_stream():
        chat = client.chats.create(model="gemini-3.6-flash")
        response_stream = chat.send_message(rag_prompt)
        
        initial_payload = {
            "Question" : payload.question,
            "Retrieved_context" : retrieved_contexts,
            "Status" : "Context Loaded"
        }
        yield json.dumps(initial_payload) + '\n'
        
        for chunk in response_stream:
            if chunk.text:
                chunk_payload = {"Answer Chunk" : chunk.text}
                yield json.dumps(chunk_payload) + '\n'
    
    return StreamingResponse(generate_stream(), media_type="application/x-ndjson")
    