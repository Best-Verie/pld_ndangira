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


def update_profile():
    """Update user profile"""
    email_or_username = input("Enter your email or username: ")

    new_nationality = input("Enter your new nationality (leave blank to keep current): ")
    new_phone = input("Enter your new phone number (leave blank to keep current): ")
    new_address = input("Enter your new address (leave blank to keep current): ")
    new_gender = input("Enter your new gender (Male/Female/Other, leave blank to keep current): ")

    # Validate gender
    if new_gender and new_gender not in ('Male', 'Female', 'Other'):
         print("Invalid gender type. Please enter 'Male' or 'Female' or 'Other'.")
         return


    update_fields = []
    if new_nationality:
        update_fields.append(f"nationality='{new_nationality}'")
    if new_phone:
        update_fields.append(f"phone='{new_phone}'")
    if new_address:
        update_fields.append(f"address='{new_address}'")
    if new_gender in ('Male', 'Female', 'Other'):
        update_fields.append(f"gender='{new_gender}'")
    
    cursor = connection.cursor()
    cursor.execute(f"SELECT id FROM users WHERE (email='{email_or_username}' OR username='{email_or_username}')")
    user_id = cursor.fetchone()

    if update_fields and user_id: 
        cursor.execute(f"UPDATE users SET {', '.join(update_fields)} WHERE id={user_id[0]}")
        connection.commit()
        print("Profile updated successfully")
        cursor.close()
    else:
        print("No changes made")


def update_account_status():
    """Update user account status"""
    email_or_username = input("Enter user's email or username: ")
    new_status = input("Enter the new account status (Active/Inactive): ")

    # Validate the new status
    if new_status not in ('Active', 'Inactive'):
        print("Invalid account status. Please enter 'Active' or 'Inactive'.")
        return

    # Execute the UPDATE query
    cursor = connection.cursor()
    cursor.execute(f"UPDATE users SET account_status='{new_status}' WHERE email='{email_or_username}' OR username='{email_or_username}'")
    if cursor.rowcount > 0:
        connection.commit()
        print("Account status updated successfully")
    else:
        print("No user found with the provided email or username")
    cursor.close()



