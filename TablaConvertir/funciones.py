from csv import *
from tkinter import messagebox
import pandas as pd

data = []

def escCab(archivoCSV):
    for i in archivoCSV:
        data.append(i)

    print(data)

def lector():
    cabecera = []
    with open ('numeros.csv', 'r') as numeros:
        count = int(0)
        
        lectorArchivo = reader(numeros)
        for i  in lectorArchivo:
            print(i)
            count += 1
            cabecera.append(i)
            print(type(lectorArchivo))

    pf = pd.read_csv('numeros.csv')

    cabecera1 = len(pf.axes[1])
    print('La cabecera contiene',cabecera1)
    print(pf.to_string())
    escCab(cabecera)
    return cabecera