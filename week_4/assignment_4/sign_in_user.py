from backend import load_user_records

# this file is used to sign in the user into the database


# This function is used to sign in the user into the database
def sign_in_user(user_id, password):
    user_records = load_user_records()

    for user in user_records:
        if user["user_id"] == user_id:
            if user.get("status") == "Deactivated":
                return None  # Account is deactivated
            elif user["password"] == password:
                return user  # Correct credentials

    return None  # Account not found or incorrect password
