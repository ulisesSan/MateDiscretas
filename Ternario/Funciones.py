import tkinter as ttk
from tkinter import messagebox

def Operaciones(entero,decimal):
    arreglo = []
    rango = 0
    print (entero)
    for i in range(len (entero)):
        if int(entero[i]) >=0 | int(entero[i]) <= 2:
            arreglo.append(entero[i] + 'x3^' + str(len(entero)-i-1))
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

    Suma(entero,decimal)
    Resultado(entero)
    Decimal(decimal)

    res = Resultado(entero), round(Decimal(decimal),len(decimal))
    print(res)
    messagebox.showinfo(message=''.join(str(res)),title="Resultado")


def Suma(dato,decimal):
    arregloEntero = []
    arregloDecimal = []
    print(dato)
    for i in range(len (dato)):
        if int(dato[i]) <=0 | int(dato[i]) <= 2 :
            arregloEntero.append(int(dato[i]) * 3** (len(dato)-i-1))
            print(arregloEntero[i])
    for j in range(len(decimal)):
        if int(decimal[i]) <=0 | int(decimal[i]) <= 2 :
            arregloDecimal.append(int(decimal[i]) * 3** (len(decimal)-(i)- len(decimal)-1))
            print(len(decimal)-(i)- len(decimal)-1)

    Resultado = arregloEntero, '.', arregloDecimal
    messagebox.showinfo(message=''.join(str(Resultado)),title=("Numeros a sumar"))


def Resultado(dato):
    resEntero = 0
    for i in range(len (dato)):
        resEntero = resEntero + int(dato[i]) * 3** (len(dato)-i-1)
    
    print(resEntero)
    #messagebox.showinfo(message='Resultado: '.join(str(resEntero)),title="Resultado")
    return(resEntero)

def Decimal(dato):
    res = 0
    for i in range(len (dato)):
        res = res + int(dato[i]) * 3** (len(dato)-(i)- len(dato)-1)
    
    print(res)
    return(res)
    #messagebox.showinfo(message='Resultado: '.join(str(res)),title="Resultado")