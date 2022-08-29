import tkinter as tk
from tkinter import ttk
from funciones import *

def window():
    mainWindow = tk.Tk()
    mainWindow.title("Es que soñe feo")
    mainWindow.geometry("600x400")

    data = lector()
    label = tk.Label(mainWindow, text = data)

    label.pack()

    mainWindow.mainloop()