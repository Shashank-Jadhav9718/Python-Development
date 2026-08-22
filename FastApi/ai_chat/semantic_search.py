import os
import numpy as np 
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def compute_cosine_similarity(vector_1, vector_2):
    dot_product = np.dot(vector_1, vector_2)
    norm_vector_1 = np.linalg.norm(vector_1)
    norm_vector_2 = np.linalg.norm(vector_2)
    return dot_product / (norm_vector_1 * norm_vector_2)

def mini_semantic_search():
    api_key = os.getenv("GEMINI_SECRET_KEY")
    if not api_key:
        raise ValueError("GEMINI_SECRET_KEY is not set in the environment variables.")
    
    client = genai.Client(api_key = api_key)
    print("🚀 Booting up the Embedding Engine...\n")
    
    documents = [
        "FastAPI is a Python framework used to create backend web servers and APIs.",
        "Dogs are highly social animals and love to play.",
        "To build AI apps, you need API keys and cloud deployment."
    ]
    print(f"📝 Original Documents: {documents}\n")
    print("🔍 Generating embeddings for the documents...\n")
    document_embeddings = []
    
    for doc in documents:
        try:
            result = client.models.embed_content(
                model='gemini-embedding-2',
                contents=doc,
                config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT")
            )
            document_embeddings.append(result.embeddings[0].values)
            print(f"✅ Successfully generated embedding for document: '{doc}'")
        except Exception as e:
            print(f"\n❌ Error generating embeddings for document '{doc}': {e}")
            return
        
    query = "How do I create a backend web server?"
    print(f"\n👤 Step 2: Search Query: '{query}'")
    query_result = client.models.embed_content(
        model='gemini-embedding-2',
        contents=query,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")
    )
    query_embedding = query_result.embeddings[0].values
    
    print("\n🔍 Computing cosine similarity between the query and each document...\n")
    for i, document_embedding in enumerate(document_embeddings):
        similarity = compute_cosine_similarity(query_embedding, document_embedding)
        print(f"Document: '{documents[i]}'")
        print(f"Cosine Similarity: {similarity:.4f}\n") 
        
if __name__ == "__main__":
    mini_semantic_search()