import re
import tkinter as tk

# This file is used to check the password and contains all the functions related to it


# this function is used to check if the password is valid or not
def is_valid_password(password):
    # Check if password meets the specified criteria
    return (
        8 <= len(password) <= 12
        and re.search(r"[A-Z]", password)
        and re.search(r"\d", password)
        and re.search(r"[a-z]", password)
        and re.search(r"[!@#$%&*]", password)
        and " " not in password
    )


# THis functions displays the error message  window if the password is not valid
def show_password_requirements_error():
    error_window = tk.Toplevel()
    error_window.title("Password Requirements Error")

    error_message = (
        "Password: A valid password should satisfy the following:\n"
        "a) It should be within 8-12 characters long.\n"
        "b) It should contain at least one upper case, one digit, and one lower case.\n"
        "c) It should contain one or more special character(s) from the list [! @ # $ % & *].\n"
        "d) No blank space will be allowed."
    )

    tk.Label(error_window, text=error_message, padx=20, pady=20).pack()

    ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
    ok_button.pack()
