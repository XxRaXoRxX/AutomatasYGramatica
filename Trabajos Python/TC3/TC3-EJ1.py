#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo en Clase N°3 - Ejercicio N°1: (a|b)*

def Ej1(string):
    #Estado A es el estado 0(inicial), Estado 2 es B y el estado 3 es C.
    estado = 1

    for i in(string):

        #Estado A
        if estado == 1:

            if i == "a":

                print("Pasamos del estado 1, al estado 2.")
                estado = 2
            
            elif i == "b":

                print("Pasamos del estado 1, al estado 3.")
                estado = 3
            
            else:

                print("Caracter incorrecto en la cadena. Saliendo...")
                estado = 0
                return

        #Estado B
        if estado == 2:

            if i == "a":

                print("Estamos en el estado 2, con un caracter a")

            elif i == "b":

                print("Pasamos del estado 2 a estado 3.")
                estado = 3
            
            else:

                print("Caracter incorrecto en la cadena. Saliendo...")
                estado = 0
                return

        #Estado C     
        if estado == 3:

            if i == "b":

                print("Estamos en el estado 3, con un caracter b")
            
            elif i ==  "a":

                print("Pasamos del estado 3 al estado 2.")
                estado = 2
            
            else:

                print("Caracter incorrecto en la cadena. Saliendo...")
                estado = 0
                return
        
    print("Estado de finalización: ", estado)

string = str(input("Ingrese la expresión regular a analizar: "))
Ej1(string)