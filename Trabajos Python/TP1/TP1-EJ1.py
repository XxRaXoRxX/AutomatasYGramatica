#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo Práctico N°1 - Ejercicio N°1: Email.
import argparse as arg
import re
import os

class Constants():
    LETRAS = "[A-z]"
    SIMBOLOS = "[-, _]"
    NUMEROS = "[0-9]"
    DOMINIOS = "[outlook, hotmail, gmail, yahoo, live]"
    PAISES = "[ru, br, sh, mx, cl]"
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

        for line in lines:
            # Quitamos el /n al final del caracter
            line = line[:-1]

            # Verificamos si es valido.
            # Verificamos si empieza con una letra
            empiezaLetra = re.search(cons.LETRAS, line[0])
            # Verificamos si tiene arroba.
            arroba = re.search("@", line)
            
            if (empiezaLetra and arroba):
                #Divido la parte del arroba
                split = re.split("@", line)

                #Verifico que tiene un solo arroba.
                if (len(split) == 2):
                    #Verifico si los dominios ingresados son correctos
                    dominio = re.findall(cons.DOMINIOS, split[1])
                    #Verifico si tiene el .com
                    com = re.findall(".com", split[1])

                    print(dominio, com)

                    print("El correo ingresado es correcto:", line)
                    continue
            
            print("El correo ingresado es incorrecto:", line)

main = Main()
main.main()