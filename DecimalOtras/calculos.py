from tkinter import messagebox

digit2Value = { "0":0, "1":1, "2": 2, "3":3, "4":4,
                "5":5, "6":6, "7":7, "8":8, "9":9, 
                "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

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

def verNum(numero):
    
    numero1 = 0
    numero2 = 0
    valueBool = False
    if len(numero) == 1:
        numero1 = numero[0]
    
    else:
        numero1 = numero[0]
        numero2 = numero[1]

    try:
        int(numero1)
        int(numero2)
        valueBool = True

    except ValueError:
        messagebox.showerror(message='Debe de introducir numeros validos')
    
    except BaseException as err:
        #Si ocurre otra clase se error lo mostramos como log
        print(f"Unexpected {err=}, {type(err)=}")
    
    return valueBool

def rango(numero,baseNum):
    rango = False
    numero1 = numero[0]
    numero2 = 0
    if len(numero) != 1:
        numero2 = numero[1]

    for i in range(len(numero1)):
        if int(numero1[i]) >= 0 | int(numero1[i]) <= int(baseNum) - 1:
            rango = True
        else:
            return False
            
        
    
    if len(numero) != 1 :
        for j in range(len(numero2)):
            if int(numero2[j]) >= 0 | int(numero2[j]) <= int(baseNum) - 1 :
                rango = True
            else:
                return False

    print('Rango',rango)
    return rango

def calculos(numero,baseNum):
    print('base en calculos:', baseNum, '\nlos numeros son: ', numero )

def arregloOperaciones(numero,base):
    arregloEntero = []
    arregloDecimal = []
    entero = numero[0]
    decimal = '0'
    if len(numero) != 1:
        decimal = numero[1]
    for i in range(len (entero)):
        #Verificamos que el numero ingresado corresponda al que queremos convertir
        arregloEntero.append(entero[i] + 'x' + str(base) + '^' + str(len(entero)-i-1)+'+')
        print(arregloEntero[i])

    for i in range(len (decimal)):
        arregloDecimal.append('+'+ decimal[i] + 'x' + str(base) + '^' + str(len(decimal)-(i)-len(decimal)-1))

    res = arregloEntero + arregloDecimal
    messagebox.showinfo(message= res)
    print(res)

def operaciones(numero,Base):
    sum = 0
    numero1 = numero[0]
    numero2 = '0'
    if len(numero) != 1:
        numero2 = numero[1]
    arregloEntero = []
    arregloDecimal = []
    
    for i in range(len (numero1)):
        if int(numero1[i]) >=0 | int(numero1[i]) <= Base :
            arregloEntero.append(int(numero1[i]) * int(Base)** (len(numero1)-i-1))
            print(arregloEntero[i])
            sum = sum +  arregloEntero[i]
    #Con la longitud del dato decimal iteramos 
    for j in range(len (str(numero2))):
        if int(numero2[j]) >=0 | int(numero2[j]) <= int(Base) :
            arregloDecimal.append(int(numero2[j]) * int(Base)** (len(numero2)-(j)- len(numero2)-1))
            sum = sum +  arregloDecimal[j]
            print(len(numero2)-(j)- len(numero2)-1)

    messagebox.showinfo(message = 'Resultado: ' + str(sum))


def numeros(numero,baseNum):
    comBase = int(base(baseNum))
    print("entra al calculo", numero ," ", baseNum, ' ',comBase)
    valueBool = verNum(numero.split('.'))
    print(valueBool)
    rangoNum = rango(numero.split('.'), comBase)

    if valueBool == True & rangoNum == True:

        arregloOperaciones(numero.split('.'),comBase)
        calculos(numero.split('.'),baseNum)
        operaciones(numero.split('.'),comBase)

    else:
        messagebox.showinfo(message = 'Numero fuera de rango, verifique la base')