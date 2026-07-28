from fastapi import FastAPI
from database import engine
import models
from routers import user, post, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="My Organized Backend")

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(post.router)
