from backend import load_user_records

# This is util function file which contains all the functions which are used in the backend


# This function checks if the username is available or not
def is_username_available(user_records, user_id):
    for user in user_records:
        if user["user_id"] == user_id:
            return False
    return True


# This function checks if the password is correct or not
def get_all_users():
    user_records = load_user_records()
    return [user["user_id"] for user in user_records]


# This function checks if the password is correct or not
def get_user_details(user_id):
    user_records = load_user_records()
    for user in user_records:
        if user["user_id"] == user_id:
            return user
    return None
