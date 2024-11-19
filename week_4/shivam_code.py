import tkinter as tk
from tkinter import ttk
import pickle as pk
filename= 'data.pkl'
with open(filename,"ab") as f:
    pass

class Person:
    def __init__(self,master) :
        self.master= master
        self.name_entry= tk.Entry(self.master)
        self.birthday_entry= tk.Entry(self.master)
        self.email_entry= tk.Entry(self.master)
        self.department_entry= tk.Entry(self.master)
        self.password_entry= tk.Entry(self.master)
        self.reenter_password_entry= tk.Entry(self.master)        
   
class Student(Person):
    def __init__(self, master):
        super().__init__(master)
        self.master.destroy()
        self.master=tk.Tk()
        self.master.title("Student Registration")
        self.master.configure(bg="black")

        self.name_text = tk.Label(self.master, text="Name:")
        self.name_text.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.birthday_text = tk.Label(self.master, text="Birthday:")
        self.birthday_text.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.birthday_entry = tk.Entry(self.master)
        self.birthday_entry.grid(row=2, column=1, padx=10, pady=10)

        options = ["Select Degree", "UG Student", "PG Student"]
        self.student_type_text = tk.Label(self.master, text="You are a :")
        self.student_type_text.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.student_type_combobox = ttk.Combobox(self.master, values=options)
        self.student_type_combobox.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        self.department_text = tk.Label(self.master, text="Department :")
        self.department_text.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        self.department_entry = tk.Entry(self.master)
        self.department_entry.grid(row=4, column=1, padx=10, pady=10)

        self.gpa_text = tk.Label(self.master, text="GPA:")
        self.gpa_text.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

        self.gpa_entry = tk.Entry(self.master)
        self.gpa_entry.grid(row=6, column=1, padx=10, pady=10)

        self.email_text = tk.Label(self.master, text="Email-ID:")
        self.email_text.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=7, column=1, padx=10, pady=10)

        self.password_text = tk.Label(self.master, text="Password:")
        self.password_text.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)

        self.password_entry = tk.Entry(self.master,show="*")
        self.password_entry.grid(row=8, column=1, padx=10, pady=10)

        self.reenter_password_text = tk.Label(self.master, text="Confirm Password:")
        self.reenter_password_text.grid(row=9, column=0, padx=10, pady=10, sticky=tk.W)

        self.reenter_password_entry = tk.Entry(self.master,show="*")
        self.reenter_password_entry.grid(row=9, column=1, padx=10, pady=10)

        self.button1 = tk.Button(self.master, text="Submit", bg="black", fg="white", font=("Arial Bold", 20),
                                  command=self.open)
        self.button1.grid(row=13, column=1, padx=10, pady=10)
    def open(self):
        if self.student_type_combobox.get() == "UG Student":
            self.open_ug_student_registration()
        elif self.student_type_combobox.get() == "PG Student":
            self.open_pg_student_registration()
        else:
            select_student_type()
    def open_ug_student_registration(self):
        if self.password_entry.get() == self.reenter_password_entry.get():
            if is_valid_password(self.password_entry.get()):
                ug_student_window = tk.Toplevel(self.master)
                ug_student_window.title("UG Student Registration")
                ug_student_window.configure(bg="black")
                
                UG_Student(ug_student_window, 
                           self.name_entry.get(), 
                           self.birthday_entry.get(),
                           self.email_entry.get(),
                           self.student_type_combobox.get(),
                           self.department_entry.get(),
                           self.gpa_entry.get(),
                           self.password_entry.get(),self.reenter_password_entry.get())
                self.master.withdraw()
            else:
                not_valid_password()
        else:
            password_not_match()
    def open_pg_student_registration(self):
        if self.password_entry.get() == self.reenter_password_entry.get():
            if is_valid_password(self.password_entry.get()):
                pg_student_window = tk.Toplevel(self.master)
                pg_student_window.title("PG Student Registration")
                pg_student_window.configure(bg="black")
                
                PG_Student(pg_student_window, 
                           self.name_entry.get(), 
                           self.birthday_entry.get(),
                           self.email_entry.get(),
                           self.student_type_combobox.get(),
                           self.department_entry.get(),
                           self.gpa_entry.get(),
                           self.password_entry.get(),self.reenter_password_entry.get())
                self.master.withdraw()
            else:
                not_valid_password()
        else:
            password_not_match()
           
class Teacher(Person):
    def __init__(self,master):
        super().__init__(master)
        self.master.destroy()
        self.master=tk.Tk()
        self.master.title("Teacher Registration")
        self.master.configure(bg="black")

        self.name_text= tk.Label(self.master,text="Name:")
        self.name_text.grid(row=0,column=0,padx=10,pady= 10,sticky=tk.W)

        self.name_entry= tk.Entry(self.master)
        self.name_entry.grid(row=0,column=1,padx=10,pady=10)

        self.subjects_text= tk.Label(self.master,text= "Subject:")
        self.subjects_text.grid(row=1,column=0,padx=10,pady=10,sticky=tk.W)

        self.subjects_entry= tk.Entry(self.master)
        self.subjects_entry.grid(row=1,column=1,padx=10,pady=10)

        self.department_text= tk.Label(self.master,text= "Department:")
        self.department_text.grid(row=2,column=0,padx=10,pady=10,sticky=tk.W)

        self.department_entry= tk.Entry(self.master)
        self.department_entry.grid(row=2,column=1,padx=10,pady=10)

        self.email_text= tk.Label(self.master,text= "Email-ID:")
        self.email_text.grid(row=3,column=0,padx=10,pady=10,sticky=tk.W)

        self.email_entry= tk.Entry(self.master)
        self.email_entry.grid(row=3,column=1,padx=10,pady=10)

        self.password_text= tk.Label(self.master,text= "Password:")
        self.password_text.grid(row=4,column=0,padx=10,pady=10,sticky=tk.W)

        self.password_entry= tk.Entry(self.master,show="*")
        self.password_entry.grid(row=4,column=1,padx=10,pady=10)

        self.confirm_password_text= tk.Label(self.master,text= "Confirm Password:")
        self.confirm_password_text.grid(row=5,column=0,padx=10,pady=10,sticky=tk.W)

        self.reenter_password_entry= tk.Entry(self.master,show="*")
        self.reenter_password_entry.grid(row=5,column=1,padx=10,pady=10)

        self.button1 = tk.Button(self.master, text = "Submit", bg = "black", fg = "white", font = ("Arial Bold", 20),command= self.submitnewteacher)
        self.button1.grid(row=6,column=1,padx= 10,pady= 10)

    def submitnewteacher(self):
        if self.password_entry.get() == self.reenter_password_entry.get():
            if is_valid_password(self.password_entry.get()):
                emailid = self.email_entry.get()
                data = []
                with open(filename, "rb") as f:
                    while True:
                        try:
                            data.append(pk.load(f))
                        except EOFError:  
                            break

                flag = True

                for record in data:
                    if record[2] == emailid : 
                        email_id_already_exists()
                        flag = False
                        break

                if flag:
                    emailid_1 =[self.name_entry.get(),self.subjects_entry.get(),self.email_entry.get(),self.department_entry.get(),self.password_entry.get()]
                    with open(filename, "ab") as f:
                        pk.dump(emailid_1, f)
                    registration_successful()
                    self.master.withdraw()
            else:
                not_valid_password()
        else:
            password_not_match()

class UG_Student(Student):
    def __init__(self, master, name, birthday, email, student_type, department, gpa, password,reenter_password):
        super().__init__(master)
        self.master.title("UG Student Registration")
        self.master.configure(bg="black")

        self.Internships_text = tk.Label(self.master, text="Internships:")
        self.Internships_text.grid(row=10, column=0, padx=10, pady=10, sticky=tk.W)

        self.Internships_entry = tk.Entry(self.master)
        self.Internships_entry.grid(row=10, column=1, padx=10, pady=10)

        self.button1 = tk.Button(self.master, text="Submit", bg="black", fg="white", font=("Arial Bold", 20),
                                  command=self.submitnewugstudent)
        self.button1.grid(row=13, column=1, padx=10, pady=10)
        self.name_entry.insert(0, name)
        self.birthday_entry.insert(0, birthday)
        self.email_entry.insert(0, email)
        self.student_type_combobox.set(student_type)
        self.department_entry.insert(0, department)
        self.gpa_entry.insert(0, gpa)
        self.password_entry.insert(0, password)
        self.reenter_password_entry.insert(0,reenter_password)

    def submitnewugstudent(self):
        if self.password_entry.get() == self.reenter_password_entry.get():
            if is_valid_password(self.password_entry.get()):
                emailid = self.email_entry.get()
                data = []
                with open(filename, "rb") as f:
                    while True:
                        try:
                            data.append(pk.load(f))
                        except EOFError:
                            break

                flag = True

                for record in data:
                    if record[2] == emailid:
                        email_id_already_exists()
                        flag = False
                        break

                if flag:
                    emailid_1 = [self.name_entry.get(), self.birthday_entry.get(), self.email_entry.get(),
                                 self.student_type_combobox.get(), self.department_entry.get(),
                                 self.gpa_entry.get(), self.password_entry.get(), self.Internships_entry.get()]
                    with open(filename, "ab") as f:
                        pk.dump(emailid_1, f)
                    registration_successful()
                    self.master.withdraw()
            else:
                not_valid_password()
                self.master.withdraw()
        else:
            password_not_match()
            self.master.withdraw()

class PG_Student(Student):
    def __init__(self, master, name, birthday, email, student_type, department, gpa, password,reenter_password):
        super().__init__(master)
        self.master.title("PG Student Registration")
        self.master.configure(bg="black")

        self.Thesis_text = tk.Label(self.master, text="Thesis:")
        self.Thesis_text.grid(row=10, column=0, padx=10, pady=10, sticky=tk.W)

        self.Thesis_entry = tk.Entry(self.master)
        self.Thesis_entry.grid(row=10, column=1, padx=10, pady=10)

        self.button1 = tk.Button(self.master, text="Submit", bg="black", fg="white", font=("Arial Bold", 20),
                                  command=self.submitnewpgstudent)
        self.button1.grid(row=13, column=1, padx=10, pady=10)
        self.name_entry.insert(0, name)
        self.birthday_entry.insert(0, birthday)
        self.email_entry.insert(0, email)
        self.student_type_combobox.set(student_type)
        self.department_entry.insert(0, department)
        self.gpa_entry.insert(0, gpa)
        self.password_entry.insert(0, password)
        self.reenter_password_entry.insert(0,reenter_password)
    def submitnewpgstudent(self):
        if self.password_entry.get() == self.reenter_password_entry.get():
            if is_valid_password(self.password_entry.get()):
                emailid = self.email_entry.get()
                data = []
                with open(filename, "rb") as f:
                    while True:
                        try:
                            data.append(pk.load(f))
                        except EOFError:
                            break

                flag = True

                for record in data:
                    if record[2] == emailid:
                        email_id_already_exists()
                        flag = False
                        break

                if flag:
                    emailid_1 = [self.name_entry.get(), self.birthday_entry.get(), self.email_entry.get(),
                                 self.student_type_combobox.get(), self.department_entry.get(),
                                 self.gpa_entry.get(), self.password_entry.get(), self.Thesis_entry.get()]
                    with open(filename, "ab") as f:
                        pk.dump(emailid_1, f)
                    registration_successful()
                    self.master.withdraw()
            else:
                not_valid_password()
                self.master.withdraw()
        else:
            password_not_match()
            self.master.withdraw()
    
class StartPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome to KGP++")
        screen_width=self.master.winfo_screenwidth()
        screen_height=self.master.winfo_screenheight()
        self.master.configure(bg = "black")     

        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
        self.master.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")
               

        self.label1 = tk.Label(self.master, text = "KGP++", font = ("Arial Bold", 40), bg = "black", fg = "white",)
        self.label1.pack()

        self.button1 = tk.Button(self.master, text = "New Registration", bg = "black", fg = "white", font = ("Arial Bold", 20),command = CallNewRegistration)
        self.button1.pack(side = tk.TOP,padx= 5,pady= 2,anchor =tk.N)
        
        self.button2 = tk.Button(self.master, text = "Login", bg = "black", fg = "white", font = ("Arial Bold", 20),command= CallLogin)
        self.button2.pack(side = tk.TOP,padx= 5,pady= 2,anchor = tk.N)
       
class NewRegistration:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("New Registration")
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        self.master.configure(bg="black")

        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
        self.master.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

        self.label1 = tk.Label(self.master, text="New Registration", font=("Arial Bold", 40), bg="black", fg="white")
        self.label1.pack()

        self.button1 = tk.Button(self.master, text="Student", bg="black", fg="white", font=("Arial Bold", 20), command=self.studentRegistration)
        self.button1.pack()

        self.button2 = tk.Button(self.master, text="Teacher", bg="black", fg="white", font=("Arial Bold", 20), command=self.teacherRegistration)
        self.button2.pack()

    def studentRegistration(self):
        Student(self.master)

    def teacherRegistration(self):
        Teacher(self.master)

class Login:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("KGP++")
        screen_width=self.master.winfo_screenwidth()
        screen_height=self.master.winfo_screenheight()
        self.master.configure(bg = "black")     

        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
        self.master.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")
               
        self.label1 = tk.Label(self.master, text = "Login", font = ("Arial Bold", 40), bg = "black", fg = "white")
        self.label1.pack()

        self.email_text = tk.Label(self.master, text='Email-ID', font=("Arial Bold", 20), bg="black", fg="white")
        self.email_text.pack()

        self.email_entry = tk.Entry(self.master, font=("Arial Bold", 20))
        self.email_entry.pack()

        self.password_text = tk.Label(self.master, text='Password', font=("Arial Bold", 20), bg="black", fg="white")
        self.password_text.pack()

        self.password_entry = tk.Entry(self.master, font=("Arial Bold", 20), show='*')
        self.password_entry.pack()
        
        self.user_text = tk.Label(self.master, text='Select User', font=("Arial Bold", 20), bg="black", fg="white")
        self.user_text.pack()
        options = ["Select", "Student", "Teacher"]
        self.user_entry= ttk.Combobox(self.master, values=options)
        self.user_entry.pack()

        self.login_button = tk.Button(self.master, text='Login', font=("Arial Bold", 20), bg="black", fg="white", command=self.search)
        self.login_button.pack(padx=10,pady=10)
    def search(self):
        f= open(filename,"rb")
        emailid= self.email_entry.get()
        password= self.password_entry.get()
        data=[]
        with open(filename,"rb") as f:
            while True:
                try:
                    data.append(pk.load(f))
                except EOFError:
                    break        
        flag = False
        if(self.user_entry.get()=="Teacher"):
            for i in data:
                if len(i)==5 and i[2]==emailid and i[4]!=password:
                    wrong_password()
                    flag= True
                    break
                elif len(i)==5 and i[2]==emailid and i[4]==password:
                    self.master.quit()
                    self.open_teacher_page(i)
                    flag= True
                    break
        else:
            for i in data:                
                if len(i)==8 and i[2]==emailid and i[6]!=password:
                    wrong_password()
                    flag=True
                    break
                elif len(i)==8 and i[2]==emailid and i[6]==password:
                    self.open_student_page(i)
                    self.master.quit()
                    flag= True
                    break
        if flag==False:
            user_not_found= tk.Tk()
            user_not_found.title("Warning")
            user_not_found.configure(bg="white")
            user_not_found.geometry("300x100")
            label1= tk.Label(user_not_found,text="User not found",bg="white",fg="black")
            label1.pack()
            button1= tk.Button(user_not_found,text="OK",bg="black",fg="white",command=user_not_found.destroy)
            button1.pack()
    def open_student_page(self,list):
        self.master.destroy()
        temp= StudentPage(list)

        temp.master.mainloop()
    def open_teacher_page(self,list):
        self.master.destroy()
        print(list)
        temp= TeacherPage(list)
        temp.master.mainloop()
  
class StudentPage(Student):
    def __init__(self,S):    
        self.master= tk.Tk()
        self.master.title("KGP++")
        self.master.configure(bg = "black")
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
        self.master.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

        self.Hello= tk.Label(self.master,text="Hello "+S[0],bg="black",fg="white",font=("Arial Bold",40),padx= 20,pady=20)
        self.Hello.pack()

        self.Edit_Details= tk.Button(self.master,text="Edit Details",bg="black",fg="white",font=("Arial Bold",20),command= self.edit_details)
        self.Edit_Details.pack(padx= 20,pady= 20)

        self.Deregister= tk.Button(self.master,text="Deregister",bg="black",fg="white",font=("Arial Bold",20),command= self.deregister)
        self.Deregister.pack(padx=20,pady= 20)

        self.See_other_Details= tk.Button(self.master,text="See other Details",bg="black",fg="white",font=("Arial Bold",20),command= self.see_other_details)
        self.See_other_Details.pack(padx=20,pady= 20)

        self.name_entry=S[0]
        self.birthday_entry=S[1]
        self.student_type_combobox=S[3]
        self.department_entry=S[4]
        self.gpa_entry=S[5]
        self.email_entry=S[2]
        self.Internships_entry=S[7]

    def see_other_details(self):
        popup=tk.Tk()
        popup.title("Personal Details")
        popup.configure(bg="white")
        popup.geometry("500x600")

        label1= tk.Label(popup,text="Name: "+self.name_entry,bg="white",fg="black")
        label1.grid(row=0,column=0,padx=10,pady=10,sticky=tk.W)
        label2= tk.Label(popup,text="Birthday: "+self.birthday_entry,bg="white",fg="black")
        label2.grid(row= 1,column=0,padx=10,pady=10,sticky=tk.W)
        label3= tk.Label(popup,text="Email-ID: "+self.email_entry,bg="white",fg="black")
        label3.grid(row= 2,column=0,padx=10,pady=10,sticky=tk.W)
        label4= tk.Label(popup,text="Department: "+self.department_entry,bg="white",fg="black")
        label4.grid(row= 3,column=0,padx=10,pady=10,sticky=tk.W)
        label5= tk.Label(popup,text="GPA: "+self.gpa_entry,bg="white",fg="black")
        label5.grid(row= 4,column=0,padx=10,pady=10,sticky=tk.W)
        label6= tk.Label(popup,text="Internships: "+self.Internships_entry,bg="white",fg="black")
        label6.grid(row= 5,column=0,padx=10,pady=10,sticky=tk.W)
        button1= tk.Button(popup,text="OK",bg="black",fg="white",command=popup.destroy)
        button1.grid(row= 6,column = 1,padx= 10,pady= 10,sticky=tk.W)

    def edit_details(self):
        edit_popup = tk.Toplevel(self.master)
        edit_popup.title("Edit Details")
        edit_popup.configure(bg="white")

        self.edit_name = tk.Entry(edit_popup)
        self.edit_name.insert(0,self.name_entry)

        self.edit_birthday = tk.Entry(edit_popup)
        self.edit_birthday.insert(0, self.birthday_entry)

        self.edit_gpa = tk.Entry(edit_popup)
        self.edit_gpa.insert(0, self.gpa_entry)
        
        self.edit_department= tk.Entry(edit_popup)
        self.edit_department.insert(0, self.department_entry)
        
        self.edit_internships= tk.Entry(edit_popup)
        self.edit_internships.insert(0, self.Internships_entry)

        name_label = tk.Label(edit_popup, text="Name:")
        name_label.grid(row=0, column=0, sticky=tk.E)
        self.edit_name.grid(row=0, column=1)

        birthday_label = tk.Label(edit_popup, text="Birthday:")
        birthday_label.grid(row=1, column=0, sticky=tk.E)
        self.edit_birthday.grid(row=1, column=1)

        gpa_label = tk.Label(edit_popup, text="GPA:")
        gpa_label.grid(row=2, column=0, sticky=tk.E)
        self.edit_gpa.grid(row=2, column=1)

        department_label = tk.Label(edit_popup, text="Department:")
        department_label.grid(row=3, column=0, sticky=tk.E)
        self.edit_department.grid(row=3, column=1)      

        internships_label = tk.Label(edit_popup, text="Internships:")
        internships_label.grid(row=4, column=0, sticky=tk.E)
        self.edit_internships.grid(row=4, column=1)         
        
        save_button = tk.Button(edit_popup, text="Save", command=self.save_changes)
        save_button.grid(row=5, column=0, columnspan=2)
       
    def save_changes(self):
        self.name_entry=self.edit_name.get()
        self.gpa_entry=self.edit_gpa.get()
        self.department_entry=self.edit_department.get()
        self.Internships_entry=self.edit_internships.get()
        self.birthday_entry=self.edit_birthday.get()       

        data = []
        with open(filename, "rb") as f:
            while True:
                try:
                    data.append(pk.load(f))
                except EOFError:
                    break
        for record in data:
            if record[2]== self.email_entry:
                record[0]= self.name_entry
                record[1]= self.birthday_entry
                record[4]= self.department_entry
                record[5]= self.gpa_entry
                record[7]= self.Internships_entry
                break
        with open(filename, "wb") as f:
            for item in data:
                pk.dump(item, f)    
        saved()
    def deregister(self):
        self.popup = tk.Toplevel(self.master)
        self.popup.title("De-Registration")
        self.popup.configure(bg="white")
        self.popup.geometry("500x150")
        label1= tk.Label(self.popup,text="Are you sure you want to deregister?",bg="white",fg="black")
        label1.pack()
        button1= tk.Button(self.popup,text="Yes",bg="black",fg="white",command=self.commands)
        button1.pack()
        button2= tk.Button(self.popup,text="No",bg="black",fg="white",command=self.popup.destroy)
        button2.pack()
    def commands(self):
        self.dereg()
        self.master.withdraw()

    def dereg(self):
        data = []
        with open(filename, "rb") as f:
            while True:
                try:
                    data.append(pk.load(f))
                except EOFError:
                    break

        for i in data:
            if i[2] == self.email_entry:
                data.remove(i)
                break

        with open(filename, "wb") as f:
            for item in data:
                pk.dump(item, f)

        Deregistered = tk.Tk()
        Deregistered.title("Deregistered")
        Deregistered.configure(bg="white")
        Deregistered.geometry("300x100")
        label1 = tk.Label(Deregistered, text="You have been deregistered", bg="white", fg="black")
        label1.pack()
        button1 = tk.Button(Deregistered, text="OK", bg="black", fg="white", command=Deregistered.destroy)
        button1.pack()

class TeacherPage(Teacher):
    def __init__(self, T):
        print(T)
        self.master= tk.Tk()
        self.master.title("KGP++")
        self.master.configure(bg = "black")
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        
        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
        self.master.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")
        
        self.Hello= tk.Label(self.master,text="Hello "+T[0], bg="black", fg="white", font=("Arial Bold", 40), padx= 20, pady=20)
        self.Hello.pack()

        self.Edit_Details= tk.Button(self.master, text="Edit Details", bg="black", fg="white", font=("Arial Bold", 20), command=self.edit_details)
        self.Edit_Details.pack(padx=20, pady=20)

        self.Deregister= tk.Button(self.master, text="Deregister", bg="black", fg="white", font=("Arial Bold", 20), command=self.deregister)
        self.Deregister.pack(padx=20, pady=20)

        self.See_other_Details= tk.Button(self.master, text="See other Details", bg="black", fg="white", font=("Arial Bold", 20), command=self.see_other_details)
        self.See_other_Details.pack(padx=20, pady=20)

        self.name_entry=T[0]
        self.subjects_entry=T[1]
        self.email_entry=T[2]
        self.department_entry=T[3]
        

    def see_other_details(self):
        popup=tk.Tk()
        popup.title("Personal Details")
        popup.configure(bg="white")
        popup.geometry("500x600")

        label1= tk.Label(popup,text="Name: "+self.name_entry,bg="white",fg="black")
        label1.grid(row=0,column=0,padx=10,pady=10,sticky=tk.W)
        label2= tk.Label(popup,text="Subjects: "+self.subjects_entry,bg="white",fg="black")
        label2.grid(row= 1,column=0,padx=10,pady=10,sticky=tk.W)
        label3= tk.Label(popup,text="Email-ID: "+self.email_entry,bg="white",fg="black")
        label3.grid(row= 2,column=0,padx=10,pady=10,sticky=tk.W)
        label4= tk.Label(popup,text="Department: "+self.department_entry,bg="white",fg="black")
        label4.grid(row= 3,column=0,padx=10,pady=10,sticky=tk.W)
        button1= tk.Button(popup,text="OK",bg="black",fg="white",command=popup.destroy)
        button1.grid(row = 4,column = 1,padx= 10,pady= 10,sticky= tk.W)
    def edit_details(self):
        edit_popup = tk.Toplevel(self.master)
        edit_popup.title("Edit Details")
        edit_popup.configure(bg="white")

        self.edit_name = tk.Entry(edit_popup)
        self.edit_name.insert(0, self.name_entry)

        self.edit_subjects = tk.Entry(edit_popup)
        self.edit_subjects.insert(0, self.subjects_entry)

        self.edit_department = tk.Entry(edit_popup)
        self.edit_department.insert(0, self.department_entry)

        name_label = tk.Label(edit_popup, text="Name:")
        name_label.grid(row=0, column=0, sticky=tk.E)
        self.edit_name.grid(row=0, column=1)

        subjects_label = tk.Label(edit_popup, text="Subjects:")
        subjects_label.grid(row=1, column=0, sticky=tk.E)
        self.edit_subjects.grid(row=1, column=1)

        department_label = tk.Label(edit_popup, text="Department:")
        department_label.grid(row=2, column=0, sticky=tk.E)
        self.edit_department.grid(row=2, column=1)

        button1= tk.Button(edit_popup,text="Save",command=self.save_changes)
        button1.grid(row=3,column=0,columnspan=2)
    def save_changes(self):
        self.name_entry=self.edit_name.get()
        self.subjects_entry=self.edit_subjects.get()
        self.department_entry=self.edit_department.get()
        data = []
        with open(filename, "rb") as f:
            while True:
                try:
                    data.append(pk.load(f))
                except EOFError:
                    break
        for record in data:
            if record[2]== self.email_entry:
                record[0]= self.name_entry
                record[1]= self.subjects_entry
                record[3]= self.department_entry
                break
        with open(filename, "wb") as f:
            for item in data:
                pk.dump(item, f)        
        saved()


    def deregister(self):
        popup= tk.Tk()
        popup.title("De-Registration")
        popup.configure(bg="white")
        popup.geometry("500x150")
        label1= tk.Label(popup,text="Are you sure you want to deregister?",bg="white",fg="black")
        label1.pack()
        button1= tk.Button(popup,text="Yes",bg="black",fg="white",command=self.commands)
        button1.pack()
        button2= tk.Button(popup,text="No",bg="black",fg="white",command=popup.destroy)
        button2.pack()
    def commands(self):
        self.dereg()
        self.master.withdraw()
        
    def dereg(self):
        data = []
        with open(filename, "rb") as f:
            while True:
                try:
                    data.append(pk.load(f))
                except EOFError:
                    break

        for i in data:
            if i[2] == self.email_entry:
                data.remove(i)
                break

        with open(filename, "wb") as f:
            for item in data:
                pk.dump(item, f)

        Deregistered = tk.Tk()
        Deregistered.title("Deregistered")
        Deregistered.configure(bg="white")
        Deregistered.geometry("300x100")
        label1 = tk.Label(Deregistered, text="You have been deregistered", bg="white", fg="black")
        label1.pack()
        button1 = tk.Button(Deregistered, text="OK", bg="black", fg="white", command=Deregistered.destroy)
        button1.pack()
   
def is_valid_password(password):
    if len(password) < 8:
        return False
    upper =False
    lower= False
    digit = False
    special= False


    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        elif char in "!@#$%^&*()_+=-?/.,:;}{][":
            special = True
    return (upper and lower and digit and special)

def CallNewRegistration():
    temp= NewRegistration()
    
def CallLogin():
    temp= Login()

def wrong_password():
    temp= tk.Tk()
    temp.title("Warning")
    temp.configure(bg="white")
    temp.geometry("300x100")
    label1= tk.Label(temp,text="Wrong Password",bg="white",fg="black")
    label1.pack()
    button1= tk.Button(temp,text="OK",bg="black",fg="white",command=temp.destroy)
    button1.pack()

def saved():
    temp= tk.Tk()
    temp.title("Success")
    temp.configure(bg="white")
    temp.geometry("300x100")
    label1= tk.Label(temp,text="Changes Saved",bg="white",fg="black")
    label1.pack()
    button1= tk.Button(temp,text="OK",bg="black",fg="white",command=temp.destroy)
    button1.pack()

def password_not_match():
    temp=tk.Tk()
    temp.title("Warning")
    temp.configure(bg="white")
    temp.geometry("300x100")
    label1= tk.Label(temp,text="Password does not match",bg="white",fg="black")
    label1.pack()
    button1= tk.Button(temp,text="OK",bg="black",fg="white",command=temp.destroy)
    button1.pack()

def not_valid_password():
    temp= tk.Tk()
    temp.title("Warning")
    temp.configure(bg="white")
    temp.geometry("300x100")
    label1= tk.Label(temp,text="Password is not valid",bg="white",fg="black")
    label1.pack()
    button1= tk.Button(temp,text="OK",bg="black",fg="white",command=temp.destroy)
    button1.pack()
    

def registration_successful():
    temp= tk.Tk()
    temp.title("Success")
    temp.configure(bg="white")
    temp.geometry("300x100")
    label1= tk.Label(temp,text="Registration Successful",bg="white",fg="black")
    label1.pack()
    button1= tk.Button(temp,text="OK",bg="black",fg="white",command=temp.destroy)
    button1.pack()

def email_id_already_exists():
    temp= tk.Tk()
    temp.title("Warning")
    temp.configure(bg="white")
    temp.geometry("300x100")
    label1= tk.Label(temp,text="Email-ID already exists",bg="white",fg="black")
    label1.pack()
    button1= tk.Button(temp,text="OK",bg="black",fg="white",command=temp.destroy)
    button1.pack()

def select_student_type():
    temp= tk.Tk()
    temp.title("Warning")
    temp.configure(bg="white")
    temp.geometry("300x100")
    label1= tk.Label(temp,text="Select Student Type",bg="white",fg="black")
    label1.pack()
    button1= tk.Button(temp,text="OK",bg="black",fg="white",command=temp.destroy)
    button1.pack()
def main():
    root = tk.Tk()
    StartPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()


