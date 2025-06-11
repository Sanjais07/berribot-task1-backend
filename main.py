# server/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from auth import login_user, register_user
from database import cursor, conn

app = FastAPI()

class LoginData(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(data: LoginData):
    try:
        return login_user(data.email, data.password)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/register")
def register(data: LoginData):
    try:
        return register_user(data.email, data.password)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users")
def get_users():
    try:
        cursor.execute("SELECT email FROM users")
        result = cursor.fetchall()
        return {"users": [row[0] for row in result]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

