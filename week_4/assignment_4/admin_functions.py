from tkinter import Toplevel, Label, messagebox
from sign_in_user import sign_in_user
from backend import load_user_records
from util_functions import get_user_details

# This file is used to perform the admin functions


# This function is the admin login function which logins the admin into the system to check the user details
def admin_login(root, admin_id, admin_password):
    print("Admin ID:", admin_id)
    print("Admin Password:", admin_password)

    admin_user = sign_in_user(admin_id, admin_password)

    if admin_user and admin_user.get("isAdmin", False):
        messagebox.showinfo("Admin Login", "Admin login successful!")
        show_all_user_accounts(root)
    else:
        messagebox.showerror("Admin Login Error", "Invalid admin credentials.")


# This function is used to show all the user accounts to the admin
def show_all_user_accounts(root):
    all_users = load_user_records()
    user_list_window = Toplevel(root)
    user_list_window.title("All User Accounts")

    for user in all_users:
        user_frame = Toplevel(root)
        user_frame.title(f"Details for {user['user_id']}")

        Label(user_frame, text=f"User ID: {user['user_id']}").pack()
        Label(user_frame, text=f"User Type: {user['user_type']}").pack()
        Label(user_frame, text=f"Address: {user['address']}").pack()
        Label(user_frame, text=f"Department: {user['department']}").pack()

        if user["user_type"] == "UG Student":
            Label(user_frame, text=f"Roll No: {user['roll_no']}").pack()
            Label(user_frame, text=f"CG: {user['cg']}").pack()
            Label(user_frame, text=f"Semester: {user['semester']}").pack()

        elif user["user_type"] == "PG Student":
            Label(user_frame, text=f"Roll No: {user['roll_no']}").pack()
            Label(user_frame, text=f"CG: {user['cg']}").pack()
            Label(user_frame, text=f"Research Area: {user['research_area']}").pack()


# This function is used to view the details of the user
def view_user_details(user_id):
    user = get_user_details(user_id)

    if user:
        details_window = Toplevel()
        details_window.title(f"Details for {user_id}")
        Label(details_window, text=f"User ID: {user['user_id']}").pack()
        Label(details_window, text=f"User Type: {user['user_type']}").pack()
        Label(details_window, text=f"Address: {user['address']}").pack()
        Label(details_window, text=f"Department: {user['department']}").pack()

        if user["user_type"] == "UG Student":
            Label(details_window, text=f"Roll No: {user['roll_no']}").pack()
            Label(details_window, text=f"CG: {user['cg']}").pack()
            Label(details_window, text=f"Semester: {user['semester']}").pack()

        elif user["user_type"] == "PG Student":
            Label(details_window, text=f"Roll No: {user['roll_no']}").pack()
            Label(details_window, text=f"CG: {user['cg']}").pack()
            Label(details_window, text=f"Research Area: {user['research_area']}").pack()

    else:
        messagebox.showerror("Error", "User details not found.")
