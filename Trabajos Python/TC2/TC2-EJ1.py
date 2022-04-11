#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo en Clase N°2 - Ejercicio N°1: (a|b)*

def Ejercicio1(input):
    estado = 0

    for i in range(len(input)):
        caracter = input[i]

        if (estado == 0):
            print("Estado 0", "caracter:", caracter)

            if (caracter == "a"):
                estado = 2
                print("Pasamos de estado 1 y 2")
            elif (caracter == "b"):
                estado = 4
                print("Pasamos de estado 3 a 4")
            elif (caracter == " "):
                estado = 5
                print("Pasamos de estado 0 a 5")
            else:
                print("Error, letra no encontrada", caracter)
                return
            
        if (estado == 2 or estado == 4):
            print("Estado", estado, "a 5")
            estado = 5

        if (estado == 5):
            if (i == (len(input) - 1)):
                print("Estado Finalizado. Estado 5")
            else:
                print("Pasamos de estado 5 a 0")
                estado = 0

valor = str(input("Ingresar input: "))
Ejercicio1(input = valor)