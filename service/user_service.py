from repositories.user_repo import get_all_users,get_user_by_email


def verify_password(email:str, password:str):
    user =  get_user_by_email(email)
    
    if user["password_hash"] == password:
        return user
    else:
        return "email correto, mas a senha está errada"



