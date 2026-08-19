import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def analyze_document():
    api_key = os.getenv("GEMINI_SECRET_KEY")
    if not api_key:
        raise ValueError("GEMINI_SECRET_KEY environment variable is not set.")
    
    client = genai.Client(api_key=api_key)
    print("🚀 Booting up the Document Analyzer...")
    
    print("📂 Uploading knowledge.txt...")
    uploaded_file = client.files.upload(file="sample.txt")
    print(f"✅ File uploaded successfully! File ID: {uploaded_file.name}")
    
    prompt = "Who is the director of Sector 7, and what is the secret password?"
    print(f"📝 Sending prompt to the model: {prompt}")
    
    try:
        response = client.models.generate_content(
            model = 'gemini-3.5-flash',
            contents = [
                types.Part.from_uri(
                    file_uri=uploaded_file.uri,
                    mime_type=uploaded_file.mime_type
                ),
                prompt
            ]
        )
        print(f"\n🧠 Gemini: {response.text}")
    except Exception as e:
        print(f"❌ An error occurred while generating content: {e}")
    finally:
        print("🧹 Cleaning up uploaded file...")
        client.files.delete(name=uploaded_file.name)
        print("✅ Cleanup complete. Exiting Document Analyzer.")
        
if __name__ == "__main__":
    analyze_document()