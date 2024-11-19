from tkinter import *
from PIL import ImageTk, Image

root = Tk()
img = ImageTk.PhotoImage(Image.open("tkinter/21.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
"""
from tkinter import *
# from PIL import Image,ImageTk 
# fr jpeg images


root = Tk()
root.title('PythonGuides')


img = PhotoImage(file='tkinter/21.png')
Label(    root,
    image=img
).pack()

root.mainloop()"""