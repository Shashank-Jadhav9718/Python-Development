from fastapi import APIRouter 
from pydantic import BaseModel , Field

router = APIRouter(prefix='/Users' , tags=["User Management"])

class CreateUser(BaseModel):
    Username : str = Field(..., min_length = 3, max_length = 8)
    email : str 
    password : str = Field(..., min_length = 8, max_length = 16 )

@router.get("/")
def get_all_users():
    return {"message": "Returning all users in the database"}

@router.get("{user_id}")
def get_specific_user(user_id : int ):
    return {"user_id": user_id, "message": "Returning specific user"}


@router.post("/")
def create_user(new_user : CreateUser):
    return new_user
