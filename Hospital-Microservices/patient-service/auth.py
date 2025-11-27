from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import datetime

JWT_SECRET = "replace-with-secure-secret"
security = HTTPBearer()

def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(hours=4)})
    return jwt.encode(to_encode, JWT_SECRET, algorithm="HS256")

def verify_token(credentials=Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
