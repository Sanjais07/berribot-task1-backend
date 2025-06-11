# server/auth.py
from database import cursor, conn
from passlib.hash import bcrypt
from fastapi import HTTPException
import jwt
import psycopg2
from psycopg2 import IntegrityError
from database import cursor, conn 

SECRET = "your_secret_key"

def login_user(email: str, password: str):
    # Debug prints
    print("Login Attempt - Email:", email)

    cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = user[0]

    # More debug prints
    print("Password entered:", password)
    print("Password from DB:", hashed_password)
    print("Match result:", bcrypt.verify(password, hashed_password))

    if not bcrypt.verify(password, hashed_password):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"token": "dummy_token"}

def register_user(email: str, password: str):
    hashed_password = bcrypt.hash(password)
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
        conn.commit()
    except IntegrityError:
        conn.rollback()
        raise HTTPException(status_code=400, detail="User already exists")
    return {"message": "User registered successfully"}

