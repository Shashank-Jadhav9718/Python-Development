from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import *
from schemas import *

router = APIRouter(
    prefix = '/users',
    tags= ['Users']
)

@router.post('/',response_model = UserResponse)
def create_user(user : UserCreate , db : Session = Depends(get_db)):
    new_user = DBUser(username=user.username , email=user.email)
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except Exception as e :
        db.rollback()
        raise HTTPException(status_code=400, detail="Username Already Exists")
    
    
    return new_user

@router.get('/',response_model = list[UserResponse])
def get_all_users(db : Session = Depends(get_db), limit : int = 10, skip : int = 0):
    users = db.query(DBUser).limit(limit).offset(skip).all()
    
    return users

@router.get('/{user_id}', response_model = UserResponse)
def get_specific_user(user_id : int , db : Session = Depends(get_db)):
    user = db.query(DBUser).filter(DBUser.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404 , detail="User Not Found")
    
    return user

@router.put('/{user_id}', response_model = UserResponse)
def update_user(user_id : int , updated_user : UserCreate, db : Session = Depends(get_db)):
    user_query = db.query(DBUser).filter(DBUser.id == user_id)
    user = user_query.first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    
    user_query.update(updated_user.model_dump() , synchronize_session=False)
    db.commit()
    
    updated = user_query.first()
    
    return updated

@router.delete("/{user_id}", )
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    
    db.delete(user)
    db.commit()
    
    return {"message": f"User {user_id} deleted successfully"} 
