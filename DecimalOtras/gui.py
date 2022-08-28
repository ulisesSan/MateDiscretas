import tkinter as tk
from tkinter import ttk
from calculos import *

def data():
    base = combo.get()
    numero = text.get()

    print(base)
    print(numero)
    numeros(numero,base)

mainWindow = tk.Tk()
mainWindow.title("Calculadora de N a decimal")
mainWindow.geometry('300x200')

n = ['Binario','Cuaternario','Octal','Hexadecimal']
combo = ttk.Combobox(mainWindow,values = n,width = 25, state = 'readonly')
label = tk.Label(mainWindow, text = 'Seleccione la base a la que desea convertir')
label1 = tk.Label(mainWindow, text = 'Introduzca el numero decimal que desea convetir')
text = tk.Entry(mainWindow,width = 25,x = 50)
button = tk.Button(mainWindow, text = 'convertir', command=data)

combo.set('Binario')
label.pack()
combo.pack()
label1.pack()
text.pack()
button.pack()

mainWindow.mainloop()