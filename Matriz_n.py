import os,sys
os.system("cls")
import random

while True:
    n = int(input("Inserte el número de columnas y filas que desea: "))
    if n >= 2 and n <= 5:
        break
    else:
        print("Debe ser un valor entre 2 y 5.")

numeros = []

columnas_filas = n*n

while len(numeros) < columnas_filas:
    unrandom = random.randint(1,100)
    numeros.append(unrandom)

pares = []

for i in numeros:
    print(i)
    if i % 2 == 0:
        pares.append(i)

lospares = len(pares)
print("Cantidad de números pares: " + str(lospares))