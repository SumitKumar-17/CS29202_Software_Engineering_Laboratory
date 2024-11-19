from backend import load_user_records, save_user_records

# This file is used to deactivate the user account in the database


# The function is used to check if the account is deactivated or not
def is_account_deactivated(user_id):
    user_records = load_user_records()
    for user in user_records:
        if user["user_id"] == user_id and user.get("status") == "Deactivated":
            return True
    return False


# This function is used to deactivate the user account in the database
def deactivate_account(user_id):
    user_records = load_user_records()
    for user in user_records:
        if user["user_id"] == user_id:
            user["status"] = "Deactivated"
            break
    save_user_records(user_records)
