#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo Práctico N°1 - Ejercicio N°3: Dirección IPV4.
#regex101
import argparse as arg
import re
import os

class Constants():
    """Abecedario del Autómata."""

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
            split = re.split(cons.PUNTO, line)

            correct = False

            # Si el rango de la ip es de 4 bloques, ingrese, sino es una ip erronea.
            if (len(split) == 4):
                correct = self.SplitBlock(cons = cons, split = split)

            if (correct == True):
                print("La IPV4 ingresada es correcto:", line)
            else:
                print("La IPV4 ingresada es incorrecto:", line)

    def SplitBlock(self,  cons, split):
        """Verifico si el dominio es correcto.

            args:
                    -cons: Constantes.
                    -split: Dominio en lista. 
        """

        for block in split:

            correct = self.VerifyBlock(cons = cons, blockRange = len(block), block = block)

            # Verifica si es correcto el bloque, en caso de que no, devuelve IP incorrecto.
            if (correct == True):
                continue
            else:
                return False

        # Si todos los casos pasaron con exito, devuelve IP correcto.
        return True

    def VerifyBlock(self, cons, blockRange, block):
        """Verifico si el bloque es correcto.

            args:
                    -cons: Constantes.
                    -blockRange: Largo del bloque de uno de los cuatro bloques de la IP.
                    -block: Uno de los bloques de la IP.
        """

        # Ejemplo 0.
        if (blockRange == 1):
            num = re.fullmatch(cons.UNDIGITO, block[0])

            if (num != None):
                return True
            else:
                return False

        # Ejemplo 00.
        elif (blockRange == 2):
            num1 = re.fullmatch(cons.UNDIGITO, block[0])
            num2 = re.fullmatch(cons.UNDIGITO, block[1])

            if (num1 != None and num2 != None):
                return True
            else:
                return False

        # Ejemplo 000.
        elif (blockRange == 3):
            num1 = re.fullmatch(cons.TRESDIGITOSPRIMERO, block[0])

            # En caso de ser vacio que retorne, sino se explota el codigo del num1.
            if (num1 == None):
                return False
            
            # Si el primer digito es 2, el segundo digito solo llega de 0 a 5, sino de 0 a 9.
            # Verificar si el segundo no es 5 sino el tercero puede llegar al 9
            if (num1.group() == "2"):
                num2 = re.fullmatch(cons.UNDIGITO, block[1])

                try:
                    num2INT = int(num2.group())
                except:
                    return False

                if (num2INT == 5):
                    num3 = re.fullmatch(cons.TRESDIGITOSSEGTER, block[2])
                elif (num2INT < 5):
                    num3 = re.fullmatch(cons.UNDIGITO, block[2])
                else:
                    return False

            else:
                num2 = re.fullmatch(cons.UNDIGITO, block[1])
                num3 = re.fullmatch(cons.UNDIGITO, block[2])

            if (num1 != None and num2 != None and num3 != None):
                return True
            else:
                return False
        
        # Ejemplo cualquier otro devuelva error.
        else:
            return False

main = Main()
main.main()