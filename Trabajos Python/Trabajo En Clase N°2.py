#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo en Clase N°2

import random as r

# Ejercicio 1: (a|b)*
def Ejercicio1(loop):
    retorno = ""
    for i in range(loop):
        retorno = Estado1EJ1(retorno = retorno)
        print("Paso", i, "retorno:", retorno)

    return retorno

def Estado1EJ1(retorno):
    random = r.random()

    if(random <= 0.5):
        retorno += "a"
    else:
        retorno += "b"

    return retorno

# Ejercicio 2: (aa|b)*(a|bb)*
def Ejercicio2(loop):
    retorno = ""
    for i in range(loop):
        retorno = Estado1EJ2(retorno = retorno)
        print("Paso", i, "retorno:", retorno)
    
    return retorno

def Estado1EJ2(retorno):
    random = r.random()
    if(random <= 0.5):
        retorno += "aa"
    else:
        retorno += "b"

    random = r.random()
    if(random <= 0.5):
        return Estado2EJ2(retorno = retorno)
    else:
        return retorno

def Estado2EJ2(retorno):
    random = r.random()
    if(random <= 0.5):
        retorno += "ab"
    else:
        retorno += "bb"

    random = r.random()
    if(random <= 0.5):
        return retorno
    else:
        return Estado1EJ2(retorno = retorno)

# loop: Es la cantidad de loopeo que ejecuto dentro del automata.
print(Ejercicio2(8))