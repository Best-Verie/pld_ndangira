from db.connection import connection

## update password
def change_password():
    """Change user password"""
    email_or_username = input("Enter your email or username: ")
    old_password = input("Enter your current password: ")
    new_password = input("Enter your new password: ")

    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM users WHERE (email='{email_or_username}' OR username='{email_or_username}') AND password='{old_password}'")
    user_id = cursor.fetchone()
    if user_id:
        cursor.execute(f"UPDATE users SET password='{new_password}' WHERE id={user_id[0]}")
        connection.commit()
        print("Password updated successfully")
    else:
        print("Invalid email/username or password")
    cursor.close()






