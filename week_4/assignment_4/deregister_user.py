from backend import load_user_records, save_user_records

# This file is used to deregister the user from the database


def deregister_user(user_id, password):
    user_records = load_user_records()

    # Find the user with matching user_id and password
    matching_users = [
        user
        for user in user_records
        if user["user_id"] == user_id and user["password"] == password
    ]

    if matching_users:
        # Remove the matching user(s)
        user_records = [user for user in user_records if user not in matching_users]
        save_user_records(user_records)
        return True
    else:
        return False
