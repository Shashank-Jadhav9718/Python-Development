from fastapi import FastAPI , HTTPException , Depends , Header
from pydantic import BaseModel , Field

app = FastAPI()

def verify_api_key(X_api_key : str = Header(None)):
    if X_api_key != "super_secret_api_key":
        raise HTTPException(status_code = 401 , detail = "Unauthorized : Invalid API key")
    
    return X_api_key

class CreateUser(BaseModel):
    Username : str = Field(..., min_length = 3, max_length = 8)
    email : str 
    password : str = Field(..., min_length = 8, max_length = 16 )
    
    
class User_response(BaseModel):
    Username : str 
    email : str
    
@app.post("/register" , response_model = User_response)
def create_user(new_user : CreateUser):
    return new_user

@app.get("/public")
def public_info():
    return {"Message For Everyone"}

@app.get("/secure_data")
def secure_data(api_key : str = Depends(verify_api_key)):
    return {
        "Message" : "Welcome To VIP access",
        "Key used" : api_key
    }
    
    