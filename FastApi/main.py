from fastapi import FastAPI , Depends , HTTPException
from pydantic import BaseModel
from sqlalchemy import Column , Integer , String
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base

class DBUser(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String)
    
Base.metadata.create_all(bind=engine)

class UserCrate(BaseModel):
    username : str
    email : str
    
class UserResponse(BaseModel):
    id : int
    username : str
    email : str
    
    class config:
        from_attributes = True
    
    
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post('/Users')
def create_user(user : UserCrate , db : Session = Depends(get_db)):
    new_user = DBUser(username=user.username , email=user.email)
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except Exception as e :
        db.rollback()
        raise HTTPException(status_code=400, detail="Username Already Exists")
    
    
    return {
        "message": "User saved securely to PostgreSQL!", 
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
    }
    
@app.get('/Users',response_model=list[UserResponse])
def get_all_users(db : Session = Depends(get_db)):
    users = db.query(DBUser).all()
    
    return users 

@app.get('/Users/{user_id}',response_model=UserResponse)
def get_specific_user(user_id : int , db : Session = Depends(get_db)):
    user = db.query(DBUser).filter(user_id == DBUser.id).first()
    
    if not user:
        raise HTTPException(status_code=404 , detail="User Not Found")
    
    return user