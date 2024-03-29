from models.user import User
from db.connection import connection


def login():
    email = input("Email/Username: ")
    password = input("Password: ")

    cursor = connection.cursor()
    cursor.execute(f"SELECT email,username FROM users"
                   f" WHERE (email='{email}' OR username='{email}') AND password='{password}'")
    user = cursor.fetchone()
    cursor.close()
    print(f"\nLogged in as: email={user[0]}, username={user[1]}")


def register():
    """New User Registration"""
    user = User()
    user.first_name = input("First Name: ")
    user.last_name = input("Last Name: ")
    user.email = input("Email: ")
    user.username = input("Username: ")
    user.password = input("Password: ")
    user.user_type = "User"

    cursor = connection.cursor()
    cursor.execute(f"SELECT email FROM users WHERE email='{user.email}'")
    if cursor.fetchone() is not None:
        print("\nEmail already taken")
        return

    cursor.execute(f"SELECT email FROM users WHERE username='{user.username}'")
    if cursor.fetchone() is not None:
        print("\nUsername already taken")
        return

    cursor.close()

    if connection.is_connected():
        query = ("INSERT INTO users(first_name, last_name, username, email, password, user_type)"
                 f"VALUES ('{user.first_name}','{user.last_name}','{user.username}','{user.email}',"
                 f"'{user.password}','{user.user_type}')")
        connection.cursor().execute(query)
        connection.commit()
