from fastapi import FastAPI 
from pydantic import BaseModel , Field

app = FastAPI()

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

