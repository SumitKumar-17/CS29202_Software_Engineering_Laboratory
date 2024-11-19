from tkinter import *

root=Tk()
root.geometry("444x233")
root.title("Sumit")

#important Label optins
# text-add the text
# bd-background
# fg-foreground
# font-sets the font
# padx- x padding
# pady- y padding
# relief- border styling-SUNKEN,RAISED,GROOVE,RIDGE

title_label=Label(text='''lorem ipsum is simply dummy text of the printing and typesetting industry.''',
                  bg='red',
                  padx=34,
                  pady=45,
                  font=("comicsansms 19 bold")
                  ,borderwidth=3,
                  relief=SUNKEN)
# title_label=Label(text='''lorem ipsum is simply dummy text of the printing and typesetting industry.''',bg='red',padx=34,pady=45,font=("comicsansms",19,"bold"))
    
# side=top,bottom,left,right
# anchor=nw,ne,sw,se

# title_label.pack(side=BOTTOM,anchor="sw")
title_label.pack(side=BOTTOM,fill=X)
root.mainloop()