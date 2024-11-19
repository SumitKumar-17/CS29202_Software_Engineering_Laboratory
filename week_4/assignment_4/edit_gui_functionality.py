from gui import *
from backend import load_user_records
from edit_user_data import edit_user_profile

# This file is used to edit he details of the user in the database


# this function is used to show all the details of the user
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


# This function is used to edit the details of the user
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
