from tkinter import *

root=Tk()

#gui_logic

# Width X Height
root.geometry("644x344")


# Width X Height
root.minsize(200,100) #min size of window take size of window
root.maxsize(1200,988) #max size of window take size of window
#keeps us in the gui window 

#Question_1-Tkinter ways to create GUi in Python 
# GUI is a collection of pac widgets 
#learning abut widgets and attributes
#we cna make cross platform GUI with tkinter 
#tkinter is a python binding to the Tk GUI toolkit
# pac blaces widgets block wise 
#grid make s agrid layout  tell th row and column number
# .dot places at a specific position
# label is widget with which user does not interact 

name=Label(text="Enter your name")
name.pack()

root.mainloop() 

