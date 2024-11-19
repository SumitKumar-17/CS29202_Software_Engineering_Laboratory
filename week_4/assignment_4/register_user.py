from backend import load_user_records, save_user_records
from password_check import is_valid_password, show_password_requirements_error
from util_functions import is_username_available

# this file is used to register the user into the database and contains all the functions related to it


# This function is used to register the user into the database
def register_user(user_id, password, user_type):
    user_records = load_user_records()

    # Check if the username is available
    if not is_username_available(user_records, user_id):
        return "Username not available"

    # Check if the password meets the specified criteria
    if not is_valid_password(password):
        show_password_requirements_error()
        return "Password does not meet the criteria"

    if is_username_available(user_records, user_id) and is_valid_password(password):
        if user_type == "Teacher":
            user_records.append(
                {
                    "user_id": user_id,
                    "password": password,
                    "user_type": user_type,
                    "isAdmin": False,
                    "address": "",
                    "department": "",
                }
            )
        elif user_type == "UG Student":
            user_records.append(
                {
                    "user_id": user_id,
                    "password": password,
                    "user_type": user_type,
                    "isAdmin": False,
                    "address": "",
                    "roll_no": "",
                    "department": "",
                    "cg": "",
                    "semester": "",
                }
            )
        elif user_type == "PG Student":
            user_records.append(
                {
                    "user_id": user_id,
                    "password": password,
                    "user_type": user_type,
                    "isAdmin": False,
                    "address": "",
                    "roll_no": "",
                    "department": "",
                    "cg": "",
                    "research_area": "",
                }
            )

        save_user_records(user_records)
        return True
    else:
        return False
