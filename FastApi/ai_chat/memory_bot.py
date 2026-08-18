import os 
from google import genai 
from google.genai import types 
from dotenv import load_dotenv

load_dotenv()

def start_chat_session():
    api_key = os.getenv("GEMINI_SECRET_KEY")
    if not api_key:
        raise ValueError("GEMINI_SECRET_KEY is not set")
    
    client = genai.Client(api_key = api_key)
    print("🚀 Gemini Chat Session Initialized (With Memory and Personality!). Type 'exit' to quit.")
    
    my_personality = """
    You are a highly polite, traditional assistant from Pune. 
    You must only speak in Marathi, regardless of what language the user types in.
    Always start your response with a respectful greeting.
    """
    chat_config = types.GenerateContentConfig(
        system_instruction=my_personality
    )
    
    models_to_try = [
        'gemini-3.7-flash', 
        'gemini-3.6-flash',
        'gemini-3.5-flash-lite'
    ]
    
    active_model = models_to_try[0]
    chat = client.chats.create(
        model=active_model,
        config=chat_config
    )
    
    while True:
        question = input("\n👤 You : ")
        
        if question.strip().lower() == "exit":
            print("Exiting Chat session")
            break
        
        success = False
        
        for model_name in models_to_try:
            try:
                if model_name != active_model:
                    past_memory = chat.get_history()
                    chat = client.chats.create(
                        model=model_name, 
                        history=past_memory,  
                        config=chat_config     
                    )
                    active_model = model_name
            
                response = chat.send_message(question)
                print(f"🧠 Gemini ({active_model}): {response.text}")
                success = True
                
                break
            
            except Exception as e:
                if '503' in str(e):
                    print(f"⚠️ {model_name} is busy. Transferring memory to fallback model...")
                    continue
                else:
                    print(f"❌ An unexpected error occurred: {e}")
                    break
                    
        if not success:
            print("❌ All models are currently experiencing high demand. Please wait a moment and try asking again.")

if __name__ == "__main__":
    start_chat_session()