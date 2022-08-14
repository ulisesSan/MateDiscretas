import tkinter as ttk
from tkinter import messagebox

def Operaciones(dato):
    arreglo = []
    print (dato)
    for i in range(len (dato)):
        if int(dato[i]) <=0 | int(dato[i]) <= 2 :
            arreglo.append(dato[i] + 'x3^' + str(len(dato)-i-1))
            print(arreglo[i])

        else:
            #If the data obtained isnt a number show a message
            otro = ttk.Tk()#instantiating tkinter
            otro.title("Error")#window title
            otro.geometry("300x90")#Size of window

            def Cerrar(): 
                otro.destroy()#Close the window using a button

            lblErr = ttk.Label(otro, text="Debe de introducir datos de entre 0 y 2")
            btnErr = ttk.Button(otro, text="Aceptar", command=Cerrar)

            lblErr.pack()
            btnErr.pack()
            break
    
    messagebox.showinfo(message='+'.join(arreglo),title="operaciones")

    print("despues de una pausa volvemos XD")

    Suma(dato)
    Resultado(dato)

def Suma(dato):
    arreglo = []
    print(dato)
    for i in range(len (dato)):
        if int(dato[i]) <=0 | int(dato[i]) <= 2 :
            arreglo.append(int(dato[i]) * 3** (len(dato)-i-1))
            print(arreglo[i])

    messagebox.showinfo(message=''.join(str(arreglo)),title=("Numeros a sumar"))


def Resultado(dato):
    res = 0
    for i in range(len (dato)):

        res = res + int(dato[i]) * 3** (len(dato)-i-1)
    
    print(res)
    messagebox.showinfo(message=''.join(str(res)),title="Resultado")