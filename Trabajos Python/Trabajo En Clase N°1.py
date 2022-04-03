#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo en Clase N°1

import re

# Ejercicio Trabajo en Clase N°1 
# Ejercicio 1:
def Ejercicio1():
    print("Ejercicio 1:", "\nDeja vacio si queres saltar al siguiente ejercicio.")
    while True:
        dato = str(input("Ingresar cadena de caracteres: "))

        if (dato == ""):
            break

        if (dato[0].isupper()):
            print("La cadena ingresada comienza con mayuscula.")
        else:
            print("La cadena ingresada no comienza con mayuscula.")

# Ejercicio 2:
def Ejercicio2():
    print("Ejercicio 2:", "\nDeja vacio si queres saltar al siguiente ejercicio.")
    while True:
        dato = str(input("Ingresar cadena de caracteres: "))

        value = "[0-9]"

        resultado = re.search(value, dato)

        if (dato == ""):
            break

        if resultado:
            print("Existe número en la cadena.")
        else:
            print("No existe número en la cadena.")

# Ejercicio 3:
def Ejercicio3():
    print("Ejercicio 3:", "\nDeja vacio si queres saltar al siguiente ejercicio.")
    while True:
        dato = str(input("Ingresar cadena de caracteres: "))

        value = "#"

        resultado = re.search(value, dato)

        if (dato == ""):
            break

        if resultado:
            print("Es un comentario de Python.")
        else:
            print("No es un comentario de Python.")

# Ejercicio 4:
def Ejercicio4():
    print("Ejercicio 4:", "\nDeja vacio si queres finalizar.")
    while True:
        dato = str(input("Ingresar cadena de caracteres: "))

        if (dato == ""):
            break

        if dato[0].isdigit():

            if(re.search("7", dato)):
                print("La cadena contiene un 7 y empieza con un número.")
            else:
                print("La cadena inicia con un número pero no tiene el simbolo 7")

        elif dato[0].isalpha():

            value = "[p, P]"

            if(re.search(value, dato)):
                print("La cadena contiene una p o P y empieza con una letra.")
            else:
                print("La cadena inicia con una letra pero no tiene una p o P.")

        else:
            print("La cadena no inicia con número ni letra.")

# Ejecución
Ejercicio1()
Ejercicio2()
Ejercicio3()
Ejercicio4()