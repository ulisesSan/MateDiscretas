#Importamos las biblotecas necesarias
from distutils.log import error
from errno import errorcode
import tkinter as ttk
from Funciones import *

def Obt():
    cont = 0
    #Obtenemos los datos de la caja de texto
    dato = T.get()

    #Verificamos si el dato obtenido contiene un punto
    for i in range(len(dato)):
        if dato[i] == '.':
            cont = 1

    #Si contiene un punto separamos la cadena
    if cont == 1:
        numero = dato.split('.')
        decimal = numero[1]
        entero = numero[0]
    else:
        entero = dato
        decimal = 0

    print(entero)
    print(decimal)

    #Verificamos que los datos no contengan literales
    try:
        int(entero)
        int(decimal)
    
        Operaciones(entero, decimal)

    except ValueError:
        #Si el dato obtenido contiene una letra mostraremos un mensaje
        messagebox.showerror("Data Error","Los datos deben ser numericos")
    
    except BaseException as err:
        #Si ocurre otra clase se error lo mostramos como log
        print(f"Unexpected {err=}, {type(err)=}")

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


raiz.mainloop() #Creamos un ciclo para que no se cierre la ventana