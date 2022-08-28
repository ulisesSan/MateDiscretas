from tkinter import messagebox


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
        messagebox.showerror(message='Debe de introducir numeros ')
    
    except BaseException as err:
        #Si ocurre otra clase se error lo mostramos como log
        print(f"Unexpected {err=}, {type(err)=}")
    
    return valueBool

def calculos(numero,baseNum):
    print('base en calculos:', baseNum, '\nlos numeros son: ', numero )



def numeros(numero,baseNum):
    comBase = base(baseNum)
    print("entra al calculo", numero ," ", baseNum, ' ',comBase)
    valueBool = verNum(numero.split('.'))
    print(valueBool)
    if valueBool == True:
        calculos(numero.split('.'),baseNum)
