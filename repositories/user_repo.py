from db import get_conn


def get_all_users():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

def get_user_by_email(email: str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email,password_hash FROM users WHERE email = %s LIMIT 1",(email,))
    users = cursor.fetchone()

    cursor.close()
    conn.close()
    return users



