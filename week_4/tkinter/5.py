from tkinter import *

root=Tk()

root.geometry("400x400")


def hello():
    print("hello tkinter button")

frame=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1=Button(frame,fg="red",text="Print now",command=hello)
b1.pack(side=LEFT,padx=45)
b2=Button(frame,fg="red",text="Print now")
b2.pack(side=LEFT)
b3=Button(frame,fg="red",text="Print now")
b3.pack(side=LEFT)




root.mainloop()