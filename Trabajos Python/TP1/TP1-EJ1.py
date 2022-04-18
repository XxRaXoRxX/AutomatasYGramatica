#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo Práctico N°1 - Ejercicio N°1: Email.
import argparse as arg
import re
import os

class Constants():
    DOMINIOS = ["outlook", "hotmail", "gmail", "yahoo", "live"]
    PAISES = ["ru", "br", "sh", "mx", "cl"]
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

        lines = archive.readlines()

        print(lines[0][:-1])


main = Main()
main.main()