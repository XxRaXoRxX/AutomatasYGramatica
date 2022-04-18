#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo en Clase N°2 - Ejercicio N°2: (aa|b)*(a|bb)*

def Ejercicio2(input):
    estado = 0

    for i in range(len(input)):
        caracter = input[i]

        if (estado == 6):
            print("Estado 6: caracter", caracter)
    
            next = FindNextValue(list = input, i = i, plus = 1)

            if (caracter == "a"):
                if (next == "a"):
                    estado = 0
                    print ("Pasamos de estado 6 a 0")
                else:
                    estado = 12
                    print ("Pasamos de estado 6 a 7 a 8 a 12")
            
            elif (caracter == "b"):
                if (next == "b"):
                    estado = 10
                    print("Pasamos de estado 6 a 9 a 10")
                    continue
                else:
                    estado = 0
                    print("Pasamos de estado 6 a 0")
            
            elif (caracter == " "):
                next2 = FindNextValue(list = input, i = i, plus = 2)

                if (next == "a"):
                    if (next2 == "a"):
                        estado = 0
                        print("Pasamos de estado 6 a 0")
                        continue;
                    else:
                        print("Error, la entrada no es correcta.")
                elif (next == "b"):
                    if (next2 == 0):
                        estado = 0
                        print("Pasamos de estado 6 a 0")
                        continue;
                    else:
                        print("Error, la entrada no es correcta.")
                else:
                    estado = 12
                    print("Pasamos de estado 6 a 12")
            else:
                print("Error, letra no encontrada", caracter)
                return
        
        if (estado == 0):
            print("Estado 0", "caracter:", caracter)

            next = FindNextValue(list = input, i = i, plus = 1)

            if (caracter == "a"):
                if (next == "a"):
                    estado = 2
                    print("Pasamos de estado 1 y 2")
                    continue
                elif (next == "b" or next == 0):
                    estado = 6
                    print("Pasamos de estado 0 a 6")
                    estado = 12
                    print("Pasamos estado 7 a 8 a 12")

            elif (caracter == "b"):
                estado = 6
                print("Pasamos de estado 4 a 5 a 6")

                if (next == 0):
                    print("Estado de Finalización: 6")
            elif (caracter == " "):
                estado = 6
                print("Pasamos de estado 0 a 6")
            else:
                print("Error, letra no encontrada", caracter)
                return
            
        if (estado == 2):
            print("Estado 2: caracter", caracter)
            if (caracter == "a"):
                print("Pasamos de estado 2 a 3 a 6")
                estado = 6
            else:
                print("Error, letra no encontrada", caracter)
                return

        if (estado == 10):
            print("Estado 10: caracter", caracter)
            if (caracter == "b"):
                print("Pasamos de estado 10 a 11 a 12")
                estado = 12
            else:
                print("Error, letra no encontrada", caracter)
                return

        if (estado == 12):
            print("Estado 12: caracter", caracter)

            next = FindNextValue(list = input, i = i, plus = 1)

            if (next == 0):
                print("Estado de Finalización 12")
                return

            estado = 6
            print("Pasamos de estado 12 a 6")
            
def FindNextValue(list, i, plus):
    try:
        return list[i + plus]
    except:
        return 0

valor = str(input("Ingresar input: "))
Ejercicio2(input = valor)