from fastapi import FastAPI
from db import get_conn
from pydantic import BaseModel 
from repositories.user_repo import get_all_users,get_user_by_email
from service.user_service import verify_password 
from models.user import UserRequestLogin  

def root():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users


app = FastAPI()

@app.get("/")
def get_users():
    all_users = get_all_users()
    return all_users

@app.post("/login")
def search_user(user:UserRequestLogin):
    teste = verify_password(user.email,user.password) 


    return teste






