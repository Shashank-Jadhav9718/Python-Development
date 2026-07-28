import os
import hashlib
from passlib.context import CryptContext
from dotenv import load_dotenv
from datetime import datetime, timedelta
from jose import jwt

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256") 
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashPassword(password: str) -> str:
    print(f"--- STARTING HASH ---")
    print(f"RAW PASSWORD LENGTH: {len(password)}")
    
    sha256_hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print(f"SHA256 HASH LENGTH: {len(sha256_hashed_password)}")
    
    return pwd_context.hash(sha256_hashed_password) 

def verifyPassword(plain_password: str, hashed_password: str) -> bool:
    sha256_hash = hashlib.sha256(plain_password.encode('utf-8')).hexdigest()
    return pwd_context.verify(sha256_hash, hashed_password)

def create_access_token(data : dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt    