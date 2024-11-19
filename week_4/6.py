from tkinter import *
# leanring about grid layout


root=Tk()
root.geometry("400x400")

user=Label(root,text="username")
password=Label(root,text="password")

user.grid()
password.grid(row=1)


def submit():
    print("submitting form")
    print("the value of username  is ",uservalue.get())
    print("the value of password  is ",passvalue.get())


# Variable classes in tkinter 
# BooleanVar,DoubleVar,IntVar,StringVar

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)


userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)



Button(text="submit",command=submit).grid()


root.mainloop()