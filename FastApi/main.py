
from fastapi import FastAPI 
from pydantic import BaseModel 

class CreateUser(BaseModel):
    username : str 
    email : str
    password : str 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI server!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"User_Id": user_id}

@app.get("/search")
def search_items(query : str = None , limit : int = 10):
    return {"Query" : query , "limit" : limit}

@app.post("/register")
def register_user(new_user : CreateUser):
    return {"message" : f"User {new_user.username} registered successfully!"}
    return {"username" : new_user.username , "email" : new_user.email}
    return {"password" : new_user.password}

