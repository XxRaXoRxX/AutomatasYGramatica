#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo Práctico N°1 - Ejercicio N°1: Email.
import argparse as arg
import re
import os

class Constants():
    """Abecedario del Autómata."""
    
    LETRAS = "[A-z]"
    #SIMBOLOS = "[- | _]"
    NUMEROS = "[0-9]"
    DOMINIOLIST = ["outlook", "hotmail", "gmail", "yahoo", "live"]
    DOMINIOS = "|".join(DOMINIOLIST)
    PAISES = "ru|br|sh|mx|cl"
    PUNTO = "[.]"
    COM = "com"
    #ru : Rusia // br: Brazil // sh: Santa Helena // mx: Mexico // cl: Chile

class Main():
    
    def main(self):
        args = self.ArgumentsConfig()

        if(args.file):
            self.EmailCheck(file = args.file)
        else:
            print("No hay archivo de referencia. Ingresa -h para mas info.")

    def ArgumentsConfig(self):
        """Genero el ArgParse y sus argumentos.

        return:
                -arguments: Devuelve los argumentos creados en el argparse.
        """

        # Generas el parser con una descripción
        parser = arg.ArgumentParser(description="Lista de comandos.")

        # Ingreso de argumentos
        parser.add_argument("-f", "--file", type=str, help="Archivo de texto que se utiliza para obtener los input.")

        # Obtener lista de argumentos en args.
        return parser.parse_args()

    def EmailCheck(self, file):
        """Verifico si el email ingresado es correcto.

        args:
                -file: Nombre del archivo a verificar. 
        """

        # Verifico si el archivo existe en el sistema.
        if (os.path.exists(file)):
            archive = open(file, "r")
        else:
            print("El archivo ingresado no existe.")
            return

        # Obtener lineas de archivo
        lines = archive.readlines()

        #Traemos las constantes
        cons = Constants()

        #Printeamos los ejemplos que usamos.
        print("Ejemplo de dominios:", cons.DOMINIOS)
        print("Ejemplo de paises:", cons.PAISES)

        for line in lines:
            # Quitamos el /n al final del caracter
            line = line[:-1]

            # Verificamos si es valido.
            # Verificamos si empieza con una letra
            empiezaLetra = re.search(cons.LETRAS, line[0])
            # Verificamos si tiene arroba.
            arroba = re.search("@", line)
            correcto = False
            
            if (empiezaLetra and arroba):
                #Divido la parte del arroba
                split = re.split("@", line)

                #Verifico que tiene un solo arroba.
                if (len(split) == 2):
                    #Dividimos despues del arroba en dos o tres partes por puntos.
                    split2 = re.split(cons.PUNTO, split[1])

                    if (len(split2) == 2):
                        correcto = VerificarDominio(len = 2, cons = cons, split = split2)
                    elif (len(split2) == 3):
                        correcto = VerificarDominio(len = 3, cons = cons, split = split2)
            
            if (correcto == True):
                print("El correo ingresado es correcto:", line)
            else:
                print("El correo ingresado es incorrecto:", line)

def VerificarDominio(len, cons, split):
    """Verifico si el dominio es correcto.

        args:
                -len: Rango del dominio.
                -cons: Constantes.
                -split: Dominio en lista. 
    """

    dominio = re.fullmatch(cons.DOMINIOS, split[0])

    com = re.fullmatch(cons.COM, split[1])

    if (len == 3):
        pais = re.fullmatch(cons.PAISES, split[2])

        if (dominio != None and com != None and pais != None):
            return True
        else:
            return False

    else:
        if (dominio != None and com != None):
            return True
        else:
            return False


main = Main()
main.main()