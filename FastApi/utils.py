import hashlib
from passlib.context import CryptContext

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