import tkinter as tk
from tkinter import messagebox
from admin_gui_login import admin_login
from admin_functions import view_user_details, show_all_user_accounts
from backend import load_user_records
from register_user import register_user
from sign_in_user import sign_in_user
from edit_user_data import edit_user_profile
from deregister_user import deregister_user
from util_functions import get_all_users, get_user_details
from deactivate_account import is_account_deactivated, deactivate_account

# This file is used to create the GUI for the user to interact with the system
# All the functions are called from the backend.py file
# This file is solely responsible for the GUI of the system


# This is the attempts left for the user to login into the system
attempts_left = 3

# This is the main window of the system
root = tk.Tk()
root.geometry("500x400")
root.title("Academic Unit Management System")

# Initialize user type variable
user_type_var = tk.StringVar(root)
user_type_var.set("Teacher")  # Default user type

# Define Entry variables for admin login
entry_admin_id = None
entry_admin_password = None


# This function is used to show the details of the user
def show_user_details(user):
    details_window = tk.Toplevel(root)
    details_window.title(f"Details for {user['user_id']}")

    # Display user details
    tk.Label(details_window, text=f"User ID: {user['user_id']}").pack()
    tk.Label(details_window, text=f"User Type: {user['user_type']}").pack()
    tk.Label(details_window, text=f"Address: {user['address']}").pack()
    tk.Label(details_window, text=f"Department: {user['department']}").pack()

    if user["user_type"] == "UG Student":
        tk.Label(details_window, text=f"Roll No: {user['roll_no']}").pack()
        tk.Label(details_window, text=f"CG: {user['cg']}").pack()
        tk.Label(details_window, text=f"Semester: {user['semester']}").pack()

    elif user["user_type"] == "PG Student":
        tk.Label(details_window, text=f"Roll No: {user['roll_no']}").pack()
        tk.Label(details_window, text=f"CG: {user['cg']}").pack()
        tk.Label(details_window, text=f"Research Area: {user['research_area']}").pack()

    # Button to edit details
    btn_edit_details = tk.Button(
        details_window,
        text="Edit Details",
        command=lambda: edit_user_details(user["user_id"]),
    )
    btn_edit_details.pack()


# On clicking the edit button this function is called to edit the details of the user
def edit_user_details(user_id):
    edit_window = tk.Toplevel(root)
    edit_window.title(f"Edit Details for {user_id}")

    user_records = load_user_records()
    user = next((u for u in user_records if u["user_id"] == user_id), None)

    if user:
        # Create Entry widgets for editing details
        tk.Label(edit_window, text="Address:").pack()
        entry_address = tk.Entry(edit_window)
        entry_address.insert(0, user["address"])
        entry_address.pack()

        tk.Label(edit_window, text="Department:").pack()
        entry_department = tk.Entry(edit_window)
        entry_department.insert(0, user["department"])
        entry_department.pack()

        if user["user_type"] == "UG Student":
            tk.Label(edit_window, text="Roll No:").pack()
            entry_roll_no = tk.Entry(edit_window)
            entry_roll_no.insert(0, user["roll_no"])
            entry_roll_no.pack()

            tk.Label(edit_window, text="CG:").pack()
            entry_cg = tk.Entry(edit_window)
            entry_cg.insert(0, user["cg"])
            entry_cg.pack()

            tk.Label(edit_window, text="Semester:").pack()
            entry_semester = tk.Entry(edit_window)
            entry_semester.insert(0, user["semester"])
            entry_semester.pack()

        elif user["user_type"] == "PG Student":
            tk.Label(edit_window, text="Roll No:").pack()
            entry_roll_no = tk.Entry(edit_window)
            entry_roll_no.insert(0, user["roll_no"])
            entry_roll_no.pack()

            tk.Label(edit_window, text="CG:").pack()
            entry_cg = tk.Entry(edit_window)
            entry_cg.insert(0, user["cg"])
            entry_cg.pack()

            tk.Label(edit_window, text="Research Area:").pack()
            entry_research_area = tk.Entry(edit_window)
            entry_research_area.insert(0, user["research_area"])
            entry_research_area.pack()

        # Function to save edited details
        def save_edited_details():
            new_data = {
                "address": entry_address.get(),
                "department": entry_department.get(),
            }

            if user["user_type"] == "UG Student":
                new_data["roll_no"] = entry_roll_no.get()
                new_data["cg"] = entry_cg.get()
                new_data["semester"] = entry_semester.get()

            elif user["user_type"] == "PG Student":
                new_data["roll_no"] = entry_roll_no.get()
                new_data["cg"] = entry_cg.get()
                new_data["research_area"] = entry_research_area.get()

            edit_user_profile(user_id, new_data)
            messagebox.showinfo("Edit Details", "Details updated successfully!")
            edit_window.destroy()

        # Button to save edited details
        btn_save = tk.Button(edit_window, text="Save", command=save_edited_details)
        btn_save.pack()
    else:
        messagebox.showerror("Error", "User not found.")


# This function is used to register the user into the database
def register_user_gui():
    user_id = entry_user_id.get()
    password = entry_password.get()
    user_type = user_type_var.get()
    registration_result = register_user(user_id, password, user_type)

    if registration_result is True:
        messagebox.showinfo("Registration", "User registered successfully")
    else:
        messagebox.showerror("Registration Error", registration_result)


# This function is used to sign in the user into the system
def sign_in_user_gui():
    global attempts_left
    user_id = entry_user_id.get()
    password = entry_password.get()

    # Check if the account is already deactivated
    if is_account_deactivated(user_id):
        messagebox.showerror(
            "Account Deactivated",
            "This account is already deactivated. Please contact the admin.",
        )
        return

    user = sign_in_user(user_id, password)

    if user:
        messagebox.showinfo("Sign In", "Sign-in successful!")
        show_user_details(user)  # Display user details on successful sign-in
        attempts_left = 3  # Reset attempts
    else:
        user_exists = any(u["user_id"] == user_id for u in load_user_records())
        if user_exists:
            # Account found but incorrect password
            attempts_left -= 1
            if attempts_left == 0:
                # Deactivate account
                deactivate_account(user_id)
                messagebox.showerror(
                    "Account Deactivated",
                    "Too many incorrect attempts. Account deactivated.",
                )
                attempts_left = 3  # Reset attempts
            else:
                messagebox.showerror(
                    "Incorrect Password",
                    f"Incorrect password. {attempts_left} attempts left.",
                )
        else:
            # Account not found
            messagebox.showerror(
                "Account Not Found", f"User account not found for user ID: {user_id}"
            )


# This function is used to deregister the user from the system
def deregister_user_gui():
    user_id = entry_user_id.get()
    password = entry_password.get()

    if deregister_user(user_id, password):
        messagebox.showinfo("Deregistration", "Deregistration successful!")
    else:
        messagebox.showerror(
            "Deregistration Error", "User not found or incorrect password."
        )


# This function is the Gui login the admin into the system
def admin_login_gui():
    global entry_admin_id, entry_admin_password
    admin_login_window = tk.Toplevel(root)
    admin_login_window.title("Admin Login")

    label_admin_id = tk.Label(admin_login_window, text="Admin ID:")
    label_admin_id.pack()

    entry_admin_id = tk.Entry(admin_login_window)
    entry_admin_id.pack()

    label_admin_password = tk.Label(admin_login_window, text="Admin Password:")
    label_admin_password.pack()

    entry_admin_password = tk.Entry(admin_login_window, show="*")
    entry_admin_password.pack()

    btn_admin_login = tk.Button(admin_login_window, text="Login", command=admin_login)
    btn_admin_login.pack()


# This function is used to login the admin into the system
def admin_login():
    admin_id = entry_admin_id.get()
    admin_password = entry_admin_password.get()

    admin_user = sign_in_user(admin_id, admin_password)

    if admin_user and admin_user["isAdmin"]:
        messagebox.showinfo("Admin Login", "Admin login successful!")
        show_all_user_accounts()
    else:
        messagebox.showerror("Admin Login Error", "Invalid admin credentials.")


# This function is used to show all the user accounts to the admin
def show_all_user_accounts():
    all_users = get_all_users()

    user_list_window = tk.Toplevel(root)
    user_list_window.title("All User Accounts")

    for user_id in all_users:
        tk.Label(user_list_window, text=f"User ID: {user_id}").pack()

        # Add a View Details button for each user
        btn_view_details = tk.Button(
            user_list_window,
            text="View Details",
            command=lambda u=user_id: view_user_details(u),
        )
        btn_view_details.pack()


# This function is used to view the details of the user
def view_user_details(user_id):
    user_details = get_user_details(user_id)

    if user_details:
        details_window = tk.Toplevel(root)
        details_window.title(f"Details for {user_details['user_id']}")

        tk.Label(details_window, text=f"User ID: {user_details['user_id']}").pack()
        tk.Label(
            details_window, text=f"User Type: {user_details.get('user_type', 'Admin')}"
        ).pack()
        tk.Label(
            details_window, text=f"Address: {user_details.get('address', '')}"
        ).pack()
        tk.Label(
            details_window, text=f"Department: {user_details.get('department', '')}"
        ).pack()

        if "user_type" in user_details:
            if user_details["user_type"] == "UG Student":
                tk.Label(
                    details_window, text=f"Roll No: {user_details.get('roll_no', '')}"
                ).pack()
                tk.Label(
                    details_window, text=f"CG: {user_details.get('cg', '')}"
                ).pack()
                tk.Label(
                    details_window, text=f"Semester: {user_details.get('semester', '')}"
                ).pack()

            elif user_details["user_type"] == "PG Student":
                tk.Label(
                    details_window, text=f"Roll No: {user_details.get('roll_no', '')}"
                ).pack()
                tk.Label(
                    details_window, text=f"CG: {user_details.get('cg', '')}"
                ).pack()
                tk.Label(
                    details_window,
                    text=f"Research Area: {user_details.get('research_area', '')}",
                ).pack()

    else:
        messagebox.showerror("Error", f"User details not found for user ID: {user_id}")


# Tkinter GUI elements
label_user_id = tk.Label(root, text="User ID:")
label_user_id.pack(pady=5)

# Entry widget for user ID
entry_user_id = tk.Entry(root)
entry_user_id.pack(pady=5)

# Entry widget for password
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

# Entry widget for password
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Dropdown for user type
label_user_type = tk.Label(root, text="User Type:")
label_user_type.pack(pady=5)

# Dropdown for user type contains the three options
user_type_options = ["Teacher", "UG Student", "PG Student"]
dropdown_user_type = tk.OptionMenu(root, user_type_var, *user_type_options)
dropdown_user_type.pack()

# Buttons for registration, sign in, deregistration and admin login
btn_register = tk.Button(
    root, text="Register", command=register_user_gui, padx=10, pady=5
)
btn_register.pack(pady=10)

btn_sign_in = tk.Button(root, text="Sign In", command=sign_in_user_gui, padx=10, pady=5)
btn_sign_in.pack(pady=10)

btn_deregister = tk.Button(
    root, text="Deregister", command=deregister_user_gui, padx=10, pady=5
)
btn_deregister.pack(pady=10)

btn_admin_login = tk.Button(
    root, text="Admin Login", command=admin_login_gui, padx=10, pady=5
)
btn_admin_login.pack(side=tk.RIGHT, padx=10, pady=10)


# Run the main loop
root.mainloop()
