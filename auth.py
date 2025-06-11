from passlib.hash import bcrypt
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import User
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def login_user(email: str, password: str):
    db: Session = next(get_db())
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not bcrypt.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"token": "dummy_token"}  # Replace with real JWT later

def register_user(email: str, password: str):
    db: Session = next(get_db())
    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = bcrypt.hash(password)
    new_user = User(email=email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}
