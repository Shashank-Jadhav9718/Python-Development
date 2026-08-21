import os 
from google import genai
from dotenv import load_dotenv

load_dotenv()

def generate_embeddings():
    api_key = os.getenv("GEMINI_SECRET_KEY")
    if not api_key:
        raise ValueError("GEMINI_SECRET_KEY is not set in the environment variables.")
    
    client = genai.Client(api_key=api_key)
    print("🚀 Booting up the Embedding Engine...\n")
    
    text_to_embed = "FastAPI is a modern, fast web framework for building APIs with Python."
    print(f"📝 Original Text: '{text_to_embed}'")
    
    try:
        result = client.models.embed_content(
        model='gemini-embedding-2',
        contents=text_to_embed,
        )
        embeddings = result.embeddings[0].values
        print(f"\n✅ Successfully generated {len(embeddings)} numerical dimensions!")
        print(f"🔢 First 5 coordinates: {embeddings[:5]}")

    except Exception as e:
        print(f"\n❌ Error generating embeddings: {e}") 

if __name__ == "__main__":
    generate_embeddings()
    