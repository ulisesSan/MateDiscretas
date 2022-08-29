from tkinter import messagebox

digit2Value = { "0":0, "1":1, "2": 2, "3":3, "4":4,
                "5":5, "6":6, "7":7, "8":8, "9":9, 
                "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

#Se seleccionan las bases
def base(base):
    match base:
        case 'Binario':
            return '2'

        case 'Cuaternario':
            return '4'

        case 'Octal':
            return '8'

        case 'Hexadecimal':
            return '16'

        case _:
            messagebox.showinfo('Algo salio mal. Contacte al desarrollador plis')

#Verificamos que lo que se halla ingresado sea un numero valido
def verNum(numero):
    sepNumeroEntero = numero[0]
    sepNumeroDecimal = '0'
    numeroEntero = 0
    numeroDecimal = 0
    valueBool = False
    if len(numero) == 1:
        for i in range(len(numero[0])):
            numeroEntero = digit2Value[sepNumeroEntero[i]]
    
    else:
        for i in range(len(numero[0])):
            for j in range(len(numero[1])-1):
                numeroDecimal = digit2Value[sepNumeroDecimal[j]]
            numeroEntero = digit2Value[sepNumeroEntero[i]]
    try:
        int(numeroEntero)
        int(numeroDecimal)
        valueBool = True

    except ValueError:
        messagebox.showerror(message='Debe de introducir numeros validos')
    
    except BaseException as err:
        #Si ocurre otra clase se error lo mostramos como log
        print(f"Unexpected {err=}, {type(err)=}")
    
    return valueBool

#Verificamos que el numero ingresado se encuentre dentro del rango de la base
def rango(numero,baseNum):
    rango = False
    numero1 = numero[0]
    numero2 = 0
    if len(numero) != 1:
        numero2 = numero[1]

    for i in range(len(numero1)):
        if int(digit2Value[numero1[i]]) >= 0 | int(digit2Value[numero1[i]]) <= int(baseNum) - 1:
            rango = True
        else:
            return False
            
        
    
    if len(numero) != 1 :
        for j in range(len(numero2)):
            if int(digit2Value[numero2[j]]) >= 0 | int(digit2Value[numero2[j]]) <= int(baseNum) - 1 :
                rango = True
            else:
                return False

    return rango

#Esto no hace nada mas que imprimir los numeros ingresados XD
   
#Genera el arreglo y muestra como va a ser la operacion 
def arregloOperaciones(numero,base):
    arregloEntero = []
    arregloDecimal = []
    entero = numero[0]
    decimal = '0'
    if len(numero) != 1:
        decimal = numero[1]
    for i in range(len (entero)):
        arregloEntero.append(str(digit2Value[entero[i]]) + 'x' + str(base) + '^' + str(len(entero)-i-1)+'+')
       
    for i in range(len (decimal)):
        arregloDecimal.append('+'+ str(digit2Value[decimal[i]]) + 'x' + str(base) + '^' + str(len(decimal)-(i)-len(decimal)-1))

    res = arregloEntero + arregloDecimal
    messagebox.showinfo(message= res)

#Hace las operaciones y la suma
def operaciones(numero,Base):
    #Se generan las operaciones pertinentes...
    sum = 0
    numero1 = numero[0]
    numero2 = '0'
    if len(numero) != 1:
        numero2 = numero[1]
    arregloEntero = []
    arregloDecimal = []
    #Con la longitud del dato entero se itera 
    for i in range(len (numero1)):
        if int(digit2Value[numero1[i]]) >=0 | int(digit2Value[numero1[i]]) <= Base :
            arregloEntero.append(int(digit2Value[numero1[i]]) * int(Base)** (len(numero1)-i-1))
            sum = sum +  arregloEntero[i]
    #Con la longitud del dato decimal iteramos 
    for j in range(len (str(numero2))):
        if int(digit2Value[numero2[j]]) >=0 | int(digit2Value[numero2[j]]) <= int(Base) :
            arregloDecimal.append(int(digit2Value[numero2[j]]) * int(Base)** (len(numero2)-(j)- len(numero2)-1))
            sum = sum +  arregloDecimal[j]

    messagebox.showinfo(message = 'Resultado: ' + str(sum))


def numeros(numero,baseNum):
    comBase = int(base(baseNum))
    valueBool = verNum(numero.split('.'))
    rangoNum = rango(numero.split('.'), comBase)

    if valueBool == True & rangoNum == True:

        arregloOperaciones(numero.split('.'),comBase)
        operaciones(numero.split('.'),comBase)

    else:
        messagebox.showinfo(message = 'Numero fuera de rango, verifique la base')