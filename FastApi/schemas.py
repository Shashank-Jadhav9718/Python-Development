from pydantic import BaseModel
from typing import List, Optional

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
    
    
class IngestLongDocRequest(BaseModel):
    source_name : Optional[str] = "manual_entry"
    text : str
    chunk_size : Optional[int] = 500
    overlap : Optional[int] = 100
    
class IngestResponse(BaseModel):
    message : str
    inserted_count : int 
    
class AskRequest(BaseModel):
    question : str
    top_k : Optional[int] = 3 

class AskResponse(BaseModel):
    question : str
    retrieved_context : list[str]
    answer : str    