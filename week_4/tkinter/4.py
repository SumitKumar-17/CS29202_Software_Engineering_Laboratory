from tkinter import *

root=Tk()

root.geometry("644x344")
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,pady=44,fill="y")

f2=Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="Project Tkinter")
l.pack(pady=144)

l=Label(f2,text="Project Tkinter 2",font="Helvetica ",fg="red",pady="142")
l.pack(pady=44)







root.mainloop()