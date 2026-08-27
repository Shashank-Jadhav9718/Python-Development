from typing import List 

def chunk_text(text : str, chunk_size : int = 150, overlap : int = 30)-> list[str]:
    if len(text) <= chunk_size:
        return [text]
    
    chunks = []
    start = 0
    step = chunk_size - overlap
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        chunks.append(chunk)
        start += step
    
    return chunks 

sample_doc = (
    "FastAPI is a modern, high-performance web framework for building APIs with Python 3.8+. "
    "It is built on top of Starlette for the web routing parts and Pydantic for data validation. "
    "When deploying in production, FastAPI applications are typically served using Uvicorn or Gunicorn "
    "to manage asynchronous worker processes efficiently."
)

chunks = chunk_text(sample_doc, chunk_size=120, overlap=30)
print(f"📄 Total characters in original text: {len(sample_doc)}")
print(f"✂️ Total chunks created: {len(chunks)}\n")
for i, piece in enumerate(chunks, start=1):
    print(f"--- Chunk {i} ({len(piece)} chars) ---")
    print(f'"{piece}"\n')