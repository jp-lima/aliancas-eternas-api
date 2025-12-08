from fastapi import FastAPI
from db import get_conn
from pydantic import BaseModel 
from repositories.user_repo import get_all_users,get_user_by_email
from service.user_service import verify_password, service_create_user  
from models.user import UserRequestLogin, UserCreateRequest   


app = FastAPI()

@app.get("/")
def get_users():
    all_users = get_all_users()
    return all_users

@app.post("/login")
def search_user(user:UserRequestLogin):
    response_login = verify_password(user.email,user.password) 

    return response_login

@app.post("/create-user")
def create(user:UserCreateRequest):

    response = service_create_user(user.email, user.password, user.name)


    return response




