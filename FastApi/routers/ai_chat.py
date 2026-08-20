import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google import genai
from schemas import chatRequest

router = APIRouter(prefix="/ai_chat", tags=["AI Chat"])
    
@router.post("/chat")
def respond_to_question(request: chatRequest):
    api_key = os.getenv("GEMINI_SECRET_KEY")
    if not api_key:
        raise HTTPException(status_code = 500, detail="GEMINI_SECRET_KEY environment variable is not set.")
    
    client = genai.Client(api_key = api_key)
    print("🚀 Gemini Chat Session Initialized (With Memory and Personality!). Type 'exit' to quit.")
    
    models_to_try = [
            'gemini-3.7-flash', 
            'gemini-3.6-flash',
            'gemini-3.5-flash-lite'
        ]
    
    while True:
        success = False
        
        for model_name in models_to_try:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=request.question
                )
                return {"answer": response.text}
                success = True
                break
            except Exception as e:
                if '503' in str(e):
                    print(f"⚠️ Model {model_name} is currently experiencing high demand. Trying the next model...")
                    continue
                else:
                    raise HTTPException(status_code=500, detail=f"❌ Error with {model_name}: {e}")

        if not success:
            raise HTTPException(status_code=503, detail="All models are currently experiencing high demand. Please try again later.")
        