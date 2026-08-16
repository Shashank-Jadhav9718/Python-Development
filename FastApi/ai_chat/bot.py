import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def initialize_ai():
    api_key = os.getenv("GEMINI_SECRET_KEY")
    if not api_key:
        raise ValueError("GEMINI_SECRET_KEY is not set")
    
    print("🚀 Gemini AI Chatbot Initialized. Type 'exit' to quit.")
    
    client = genai.Client(api_key=api_key)
    
    models_to_try = [
        'gemini-3.7-flash', 
        'gemini-3.6-flash',
        'gemini-3.5-flash-lite'
    ]
    
    while True:
        question = input("\n👤 You: ")
        
        if question.lower() == 'exit':
            print("Exiting the chat.")
            break
            
        success = False
        
        for model_name in models_to_try:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=question
                )
                print(f"🧠 Gemini ({model_name}): {response.text}")
                success = True
                
                break 
                
            except Exception as e:
                if '503' in str(e):
                    print(f"⚠️ {model_name} is currently busy. Trying fallback model...")
                    continue 
                else:
                    print(f"❌ An unexpected error occurred: {e}")
                    break
                    
        if not success:
            print("❌ All models are currently experiencing high demand. Please wait a moment and try asking again.")

if __name__ == "__main__":
    initialize_ai()