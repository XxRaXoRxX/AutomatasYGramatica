#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo Práctico N°1 - Ejercicio N°3: Dirección IPV4.
#regex101
import argparse as arg
import re
import os

class Constants():
    UNDIGITO = "[0-9]"
    TRESDIGITOSPRIMERO = "[0-2]"
    TRESDIGITOSSEGTER = "[0-5]"
    PUNTO = "[.]"

class Main():
    
    def main(self):
        args = self.ArgumentsConfig()

        if(args.file):
            self.IPV4Check(file = args.file)
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

    def IPV4Check(self, file):
        """Verifico si la URL ingresado es correcto.

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

            #Hacemos un split con un punto.
            split = re.split(cons.PUNTOS, line)

            correcto = False

            if (len(split) == 4):
                correcto = VerificarIP(cons = cons, split = split)

            if (correcto == True):
                print("La URL ingresado es correcto:", line)
            else:
                print("La URL ingresado es incorrecto:", line)

def VerificarIP(cons, split):
    """Verifico si el dominio es correcto.

        args:
                -cons: Constantes.
                -split: Dominio en lista. 
    """

    for bloque in split:

        for i in range(len(bloque)):
            #num = re.search(cons., bloque[i])
            pass
    
def VerificarProtocolo(cons, split):
    """Verifico si el dominio es correcto.

    args:
        -cons: Constantes.
        -split: Dominio en lista. 
    """
    protocolo = re.fullmatch(cons.PROTOCOLO, split)

    return protocolo != None

main = Main()
main.main()