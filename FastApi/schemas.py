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
    password : str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    posts: List[PostResponse] = [] 

    class Config:
        from_attributes = True