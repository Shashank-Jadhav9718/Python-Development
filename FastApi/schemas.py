from pydantic import BaseModel
from typing import List

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True 

class UserBase(BaseModel):
    username: str
    email: str
    

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    posts: List[PostResponse] = [] 

    class Config:
        from_attributes = True
        
class chatRequest(BaseModel):
    question : str
    
    
class IngestRequest(BaseModel):
    documents : List[str]
    
class IngestResponse(BaseModel):
    message : str
    inserted_count : int 
    
class AskRequest(BaseModel):
    question : str

class AskResponse(BaseModel):
    question : str
    retrieved_context : str
    answer : str