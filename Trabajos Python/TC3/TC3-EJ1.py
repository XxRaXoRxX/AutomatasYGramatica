#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo en Clase N°3 - Ejercicio N°1: (a|b)*

def Ejercicio1(input):
    estado = "A"

    for i in range(len(input)):
        caracter = input[i]

        if (estado == "A"):
            print("Estado A", "caracter:", caracter)
            
            
        if (estado == "B"):
            print("Estado B", "caracter:", caracter)

            
        if (estado == "C"):
            print("Estado C", "caracter:", caracter)


            

valor = str(input("Ingresar input: "))
Ejercicio1(input = valor)