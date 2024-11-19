from gui import *
from deregister_user import deregister_user

# This file contains the GUI for the deregister user page


def deregister_user_gui():
    user_id = entry_user_id.get()
    password = entry_password.get()

    if deregister_user(user_id, password):
        messagebox.showinfo("Deregistration", "Deregistration successful!")
    else:
        messagebox.showerror(
            "Deregistration Error", "User not found or incorrect password."
        )
