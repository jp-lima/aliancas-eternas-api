from repositories.user_repo import get_all_users,get_user_by_email, post_new_user   
from utils.password import create_hash


def verify_password(email:str, password:str):
    user =  get_user_by_email(email)
    
    if user["password_hash"] == password:
        return user
    else:
        return "email correto, mas a senha está errada"


def service_create_user (email:str, password:str, name:str):
    
    hashed_password = create_hash(password)


    post_new_user("000000323", name,email, hashed_password, "2025:2828", "")
 
    return "user criado"
