from email.errors import MessageError
import tkinter as ttk
from tkinter import messagebox

def Operaciones(entero,decimal):
    #Obtenemos los datos de main
    #Declaramos un arreglo
    arreglo = []

    for i in range(len (entero)):
        #Verificamos que el numero ingresado corresponda al que queremos convertir
        if int(entero[i]) >=0 | int(entero[i]) <= 2:
            #Lenamos el arreglo con una cadena la cual contiene la operacion a realizar
            arreglo.append(entero[i] + 'x3^' + str(len(entero)-i-1))
            print(arreglo[i])

        else:
            #Si el dato que obtenemos no esta dentro de nuestro parametro
            #Mostramos un mensaje
            messagebox.showerror("Fuera de rango","Debe de ingresar numeros de 0 a 2")
            break
    
    #Mostramos las operaciones que se van a hacer
    messagebox.showinfo(message='+'.join(arreglo),title="operaciones")

    #Mandamos los datos a las funciones
    Suma(entero,decimal)
    Resultado(entero)
    Decimal(decimal)

    #Tomamos la informacion ya procesada y lo guardamos en una variable
    res = Resultado(entero) + round(Decimal(decimal),len(decimal))
    print(res)
    #Mostramos el resultado
    messagebox.showinfo(message=''.join(str(res)),title="Resultado")


def Suma(dato,decimal):
    #Declaramos dos arreglos
    arregloEntero = []
    arregloDecimal = []
    #Con la longitud del dato entero iteramos 
    for i in range(len (dato)):
        if int(dato[i]) <=0 | int(dato[i]) <= 2 :
            arregloEntero.append(int(dato[i]) * 3** (len(dato)-i-1))
            print(arregloEntero[i])
    #Con la longitud del dato decimal iteramos 
    for j in range(len(decimal)):
        if int(decimal[i]) <=0 | int(decimal[i]) <= 2 :
            arregloDecimal.append(int(decimal[i]) * 3** (len(decimal)-(i)- len(decimal)-1))
            print(len(decimal)-(i)- len(decimal)-1)

    #Mostramos los numeros que vamos a sumar
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