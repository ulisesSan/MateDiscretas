from distutils.log import error
from errno import errorcode
import tkinter as ttk
from Funciones import *

def Obt():
    cont = 0
    #getting data from text box
    dato = T.get();
    for i in range(len(dato)):
        if dato[i] == '.':
            cont = 1

    if cont == 1:
        numero = dato.split('.')
        decimal = numero[1]
        entero = numero[0]
    else:
        numero = dato.split('.')
        entero = numero[0]
        decimal = 0

    print(entero)
    print(decimal)

    #verification of data obtained
    try:
        int(entero)
        int(decimal)
        Operaciones(entero, decimal)

    except:
        #If the data obtained isnt a number show a message
        otro = ttk.Tk()#instantiating tkinter
        otro.title("Error")#window title
        otro.geometry("300x95")#Size of window

        def Cerrar(): 
            otro.destroy()#Close the window using a button

        lblErr = ttk.Label(otro, text="Debe de introducir datos numericos")
        btnErr = ttk.Button(otro, text="Aceptar", command=Cerrar)

        lblErr.pack()
        btnErr.pack()

raiz = ttk.Tk() #instantiating tkinter
raiz.title("Calculadora") #window title
raiz.geometry("300x200") #Size of window

T = ttk.Entry(raiz, width = 25, x=50) #Creating a text box
lbl = ttk.Label(raiz, text = "Introduzca el numero ternario \n que desea convertir") #Creating a Label
btn = ttk.Button(raiz, text="Convertir",command=Obt) #Creating a button

#Showing evrything
lbl.pack()
T.pack()
btn.pack()


raiz.mainloop() #We made a loop because only show the window one second (or less)