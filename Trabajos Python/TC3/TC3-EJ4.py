#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo en Clase N°3 - Ejercicio N°4: (a|b)*abb
# Estado "A": 0 // "B": 1 // "C": 2 // "D": 3 // "E": 4

def Ejercicio4(input):
    estado = 0

    for i in range(len(input)):
        caracter = input[i]

        try:
            sigValor = input[i + 1]
        except:
            sigValor = 0

        #Estado A
        if (estado == 0):
            print("Estado A", "caracter:", caracter)
            if (caracter == "a"):
                estado = CambioEstado(actual = estado, cambio = 1, sigValor = sigValor)
                continue
            elif (caracter == "b"):
                estado = CambioEstado(actual = estado, cambio = 2, sigValor = sigValor)
                continue
            else:
                Error(caracter = caracter)
                return
            
        #Estado B
        if (estado == 1):
            print("Estado B", "caracter:", caracter)
            if (caracter == "a"):
                estado = CambioEstado(actual = estado, cambio = estado, sigValor = sigValor)
                continue
            elif (caracter == "b"):
                estado = CambioEstado(actual = estado, cambio = 3, sigValor = sigValor)
                continue
            else:
                Error(caracter = caracter)
                return

        #Estado C
        if (estado == 2):
            print("Estado C", "caracter:", caracter)
            if (caracter == "a"):
                estado = CambioEstado(actual = estado, cambio = 1, sigValor = sigValor)
                continue
            elif (caracter == "b"):
                estado = CambioEstado(actual = estado, cambio = estado, sigValor = sigValor)
                continue
            else:
                Error(caracter = caracter)
                return

        #Estado D
        if (estado == 3):
            print("Estado D", "caracter:", caracter)
            if (caracter == "a"):
                estado = CambioEstado(actual = estado, cambio = 1, sigValor = sigValor)
                continue
            elif (caracter == "b"):
                estado = CambioEstado(actual = estado, cambio = 4, sigValor = sigValor)
                continue
            else:
                Error(caracter = caracter)
                return

        #Estado E
        if (estado == 4):
            print("Estado E", "caracter:", caracter)
            if (caracter == "a"):
                estado = CambioEstado(actual = estado, cambio = 1, sigValor = sigValor)
                continue
            elif (caracter == "b"):
                estado = CambioEstado(actual = estado, cambio = 2, sigValor = sigValor)
                continue
            else:
                Error(caracter = caracter)
                return

def Error(caracter):
    print("Error, caracter incorrecto:", caracter)

def CambioEstado(actual, cambio, sigValor):
    if (actual == 0):
        actual = "A"
    elif (actual == 1):
        actual = "B"
    elif (actual == 2):
        actual = "C"
    elif (actual == 3):
        actual = "D"
    elif (actual == 4):
        actual = "E"

    if (cambio == 0):
        cambioLetra = "A"
    elif (cambio == 1):
        cambioLetra = "B"
    elif (cambio == 2):
        cambioLetra = "C"
    elif (cambio == 3):
        cambioLetra = "D"
    elif (cambio == 4):
        cambioLetra = "E"

    print(f"Pasando de estado {actual} a {cambioLetra}") 

    if (sigValor == 0 and cambio == 4):
        print(f"Estado de finalización: {cambioLetra}")
    elif (sigValor == 0):
        print(f"Error, finaliza en un estado incorrecto: {cambioLetra}")

    return cambio

valor = str(input("Ingresar input: "))
Ejercicio4(input = valor)