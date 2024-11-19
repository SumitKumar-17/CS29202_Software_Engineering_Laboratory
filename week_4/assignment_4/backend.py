# The file backend.py contains the functions that are used to load and save the user data in the database.
import json

USER_DATA_FILE = "user_data.json"


def load_user_records():
    try:
        with open(USER_DATA_FILE, "r") as file:
            user_records = json.load(file)
    except FileNotFoundError:
        user_records = []
    return user_records


def save_user_records(user_records):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(user_records, file)
