import os
from google import genai
from sqlalchemy import create_engine, Text, Column, Integer, select
from sqlalchemy.orm import declarative_base, sessionmaker
from pgvector.sqlalchemy import Vector 
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_URL = os.getenv('DATABASE_URL')

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    embedding = Column(Vector(3072), nullable=False)
    
def pg_vector_pipeline():
    api_key = os.getenv('GEMINI_SECRET_KEY')
    if not api_key:
        raise ValueError("GEMINI_SECRET_KEY is missing from .env.")
    
    client = genai.Client(api_key=api_key)
    print("🚀 Booting up the Embedding Engine...\n")

    print("🛠️ Syncing tables to PostgreSQL...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        db.query(Document).delete()
        db.commit()
        
        documents = [
            "FastAPI is a Python framework used to create backend web servers and APIs.",
            "To create a backend web server in Python, you can use FastAPI by installing it with 'pip install fastapi uvicorn' and defining endpoints using standard Python functions.",
            "Dogs are highly social animals and love to play.",
            "To build AI apps, you need API keys and cloud deployment."
        ]

        print("🔍 Generating embeddings and inserting into pgvector...")
        for doc in documents:
            result = client.models.embed_content(
                model='gemini-embedding-2',
                contents=doc
            )    
            embeddings = result.embeddings[0].values
            
            db_doc = Document(content=doc , embedding=embeddings)
            db.add(db_doc)
            
        db.commit()
        print("✅ Data successfully saved!\n")
        
        user_question = "How do I create a backend web server?"
        print(f"👤 Search Query: '{user_question}'")
        
        query_result=client.models.embed_content(
            model='gemini-embedding-2',
            contents=user_question
        )
        query_vector = query_result.embeddings[0].values
        
        stmt = select(Document).order_by(
            Document.embedding.cosine_distance(query_vector)
        ).limit(1)
        
        top_match = db.execute(stmt).scalars().first()
        print(f"\n🏆 Top Database Match: '{top_match.content}'")
        
        print("\n🧠 AI is reading the context and generating an answer...")
        
        rag_prompt = f"""
        You are a highly technical assistant. You must answer the user's question using ONLY the information provided in the Context below. 
        If the answer is not contained in the Context, say "I do not have that information in my database.
        
        Context:
        {top_match.content}
        
        User Question:
        {user_question}
        """
        chat = client.chats.create(model="gemini-3.6-flash")
        final_response = chat.send_message(rag_prompt)        
        print(f"\n🤖 Final AI Answer:\n{final_response.text}")
        
    finally:
        db.close()
        
        
if __name__ == "__main__":
    pg_vector_pipeline()