from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from database import Base

class DBUser(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False, server_default='temp_password')

    posts = relationship("DBPost", back_populates="owner", cascade="all, delete")


class DBPost(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    owner = relationship("DBUser", back_populates="posts")
    
class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    embeddings = Column(Vector(3072), nullable=False)