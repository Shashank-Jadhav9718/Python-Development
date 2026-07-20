from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(
    tags=["Posts"]
)

@router.post("/users/{user_id}/posts", response_model=schemas.PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(user_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    
    user = db.query(models.DBUser).filter(models.DBUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_post = models.DBPost(title=post.title, content=post.content, owner_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post