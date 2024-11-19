import tkinter as tk
from tkinter import ttk;
import numpy as np

root=tk.Tk()
root.geometry("500x400")
root.title("Python Imaging")


createDataFile=ttk.Button(
    root,
    text="Create Data File",
)
createDataFile.pack()

readintvalue = tk.Entry(root)
readintvalue.pack(pady=5)

