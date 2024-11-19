from backend import load_user_records, save_user_records

# this file is used to edit the user data in the database


# This function is used to edit the user data in the database
def edit_user_profile(user_id, new_data):
    user_records = load_user_records()
    for user in user_records:
        if user["user_id"] == user_id:
            user.update(new_data)
            break
    save_user_records(user_records)
