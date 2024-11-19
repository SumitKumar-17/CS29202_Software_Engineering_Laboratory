from tkinter import Toplevel, Label, Entry, Button
from admin_functions import admin_login

# The function is used to create the GUI for admin login


def admin_login_gui(root):
    admin_login_window = Toplevel(root)
    admin_login_window.title("Admin Login")

    label_admin_id = Label(admin_login_window, text="Admin ID:")
    label_admin_id.pack()

    entry_admin_id = Entry(admin_login_window)
    entry_admin_id.pack()

    label_admin_password = Label(admin_login_window, text="Admin Password:")
    label_admin_password.pack()

    entry_admin_password = Entry(admin_login_window, show="*")
    entry_admin_password.pack()

    btn_admin_login = Button(
        admin_login_window,
        text="Login",
        command=lambda: admin_login(
            root, entry_admin_id.get(), entry_admin_password.get()
        ),
    )
    btn_admin_login.pack()
