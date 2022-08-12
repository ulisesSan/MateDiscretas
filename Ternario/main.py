import tkinter as ttk
from Funciones import *
from unittest.util import _MAX_LENGTH

def Obt():
    dato = T.get("1.0","end")
    

    try:
        int(dato)
        Operaciones(dato)
    except:
        otro = ttk.Tk()
        otro.title("Error")
        otro.geometry("300x90")

        def Cerrar():
            otro.destroy()

        lblErr = ttk.Label(otro, text="Debe de introducir datos numericos")
        btnErr = ttk.Button(otro, text="Aceptar", command=Cerrar)

        lblErr.pack()
        btnErr.pack()

raiz = ttk.Tk()
raiz.title("Calculadora") #titulo de la ventana
raiz.geometry("300x200")

#entrada = ttk.Text()#se crea caja de texto
#entrada.grid(row=0, column=1)#se le da un lugar a la caja de texto

T = ttk.Text(raiz, height = 1, width = 25, x=50, y= 100,)#Se genera caja de texto
lbl = ttk.Label(raiz, text = "Introduzca el numero que descea convertir")#se genera etiqueta
btn = ttk.Button(raiz, text="Convertir",command=Obt)



lbl.pack()
T.pack()
btn.pack()

raiz.mainloop()