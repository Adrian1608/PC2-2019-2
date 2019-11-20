import os,sys
os.system("cls")

personas = []
sexo = []
edad = []
hombres = 0
mujeres = 0

while len(personas) < 5:

    nombre = input("Ingrese el nombre del participante: ")

    while True:
        genero = input("Ingrese el género del participante: ")
        genero = genero.lower()
        if genero == "hombre":
            hombres += 1
            break
        if genero == "mujer":
            mujeres += 1
            break
        else:
            print("Ingrese un género válido: Hombre o Mujer.")

    while True:
        años = int(input("Ingrese la edad del participante: "))
        if años >= 5 and años <= 17:
            personas.append(nombre)
            sexo.append(genero)
            edad.append(años)
            break
        else:
            print("Ingresar una edad entre 5 y 17 años.")

largo = len(personas)

print("")
print("Lista de participantes:" + "\n")
for i in range(0, largo):
    print("Participante: " + personas[i] + ". Género: " + sexo[i] + ". Edad: " + str(edad[i]) + ".")

print("Cantidad de hombres: " + str(hombres) + ". Cantidad de mujeres: " + str(mujeres))

total = 0
for i in edad:
    total += i

promedio = total/largo
print("Promedio de edades: " + str(promedio) + "\n")