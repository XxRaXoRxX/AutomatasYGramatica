#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo Práctico N°1 - Ejercicio N°4: Contraseña Segura.
#regex101
import argparse as arg
import re
import os

class Constants():
    """Abecedario del Autómata."""

    MAYUSCULA = "[A-Z]"
    MINUSCULA = "[a-z]"
    SIMBOLO = "[_|-|*|^|$]"
    NUMERO = "[0-9]"
    LONGITUD = 8 # Longitud de la contraseña minima.

class Main():
    
    def main(self):
        args = self.ArgumentsConfig()

        if(args.file):
            self.SecurityPassword(file = args.file)
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

    def SecurityPassword(self, file):
        """Verifico si la contraseña es correcta.

        args:
                -file: Nombre del archivo a verificar. 
        """
        
        # Verifico si el archivo existe.
        if (os.path.exists(file)):
            archive = open(file, "r")
        else:
            print("El archivo ingresado no existe.")
            return

        # Obtener lineas de archivo
        lines = archive.readlines()

        #Traemos las constantes
        cons = Constants()

        for line in lines:
            # Quitamos el /n al final del caracter
            line = line[:-1]

            correct = False

            correct = self.Security(cons = cons, password = line)

            if (correct == True):
                print("La contraseña ingresada es correcto:", line)
            else:
                print("La contraseña ingresada es incorrecto:", line)

    def Security(self, cons, password):
        """Verifico si la contraseña cumple con los requisitos.

        args:
                -cons: Constantes.
                -password: Contraseña.
        """
        
        #Verifico si hay un mayuscula.
        capital = re.search(cons.MAYUSCULA, password)
        #Verifico si hay una minuscula.
        lower = re.search(cons.MINUSCULA, password)
        #Verifico si hay un simbolo.
        symbol = re.search(cons.SIMBOLO, password)
        #Verifico si hay un número.
        num = re.search(cons.NUMERO, password)
        #Verifico si tiene un rango de ocho digitos.
        range = len(password) >= cons.LONGITUD

        if ((capital and lower and num and symbol) != None and range):
            return True
        else:
            return False

main = Main()
main.main()