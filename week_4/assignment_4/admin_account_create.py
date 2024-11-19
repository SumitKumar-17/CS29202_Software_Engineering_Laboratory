from backend import load_user_records, save_user_records

# This file is used to create the admin account in the database


def create_admin_account(admin_id, admin_password):
    user_records = load_user_records()
    # Check if admin account already exists
    for user in user_records:
        if user["user_id"] == admin_id and user["isAdmin"]:
            return False

    # Create admin account
    user_records.append(
        {"user_id": admin_id, "password": admin_password, "isAdmin": True}
    )
    save_user_records(user_records)
    return True
