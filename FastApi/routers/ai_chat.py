import os
from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from google import genai
from schemas import chatRequest, IngestRequest, IngestResponse, AskRequest, AskResponse
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

@router.post("/document/ingest", response_model=IngestResponse, status_code=status.HTTP_201_CREATED)
def ingest_document(payload : IngestRequest, db : Session = Depends(get_db)):
    if not payload.documents:
        raise HTTPException(status_code=404, detail="Document list cannot be empty.")
    
    inserted = 0
    
    for doc in payload.documents:
        result = client.models.embed_content(
            model="gemini-embedding-2",
            contents=doc
        )
        embeddings = result.embeddings[0].values
        
        db_doc = Document(content=doc, embeddings=embeddings)
        db.add(db_doc)
        inserted += 1
    
    db.commit()
    return IngestResponse(message="Documents stored.", inserted_count=inserted)

@router.post('/rag/ask', response_model=AskResponse)
def ask_question(payload : AskRequest , db : Session = Depends(get_db)):
    query_result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=payload.question
    )
    query_embeddings = query_result.embeddings[0].values
    
    stmt = select(Document).order_by(
        Document.embeddings.cosine_distance(query_embeddings)
    ).limit(1)
    
    top_response = db.execute(stmt).scalars().first()
    if not top_response:
        raise HTTPException(status_code=404, detail="Database empty.")
    
    rag_prompt = f"""
    You are a technical assistant. Answer the question using ONLY the provided Context.
    If the context does not contain enough information, respond exactly: "I do not have that information in my database."

    Context:
    {top_response.content}

    User Question:
    {payload.question}
    """
    
    chat = client.chats.create(model="gemini-3.6-flash")
    ai_response = chat.send_message(rag_prompt)
    
    return AskResponse(
        question=payload.question,
        retrieved_context=top_response.content,
        answer=ai_response.text.strip()
    )
    