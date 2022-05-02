#Autómatas y Gramáticas -Universidad de Mendoza-
#Alumnos: Marcos Miglierina - Alexis Lino
# Trabajo Práctico N°1 - Ejercicio N°2: URL.
import argparse as arg
import re
import os

class Constants():
    """Abecedario del Autómata."""

    PROTOCOLO = "http|https" #No obligatorio
    WWW = "www" #No obligatorio
    DOMINIO = "com|net|gob|us|fr" #obligatorio
    DOMINIOBARRA = "com/|net/|gob/|us/|fr/"
    PAIS = "ru|br|sh|mx|cl"
    PUNTO = "[.]"
    SEPARADOR = "://"

class Main():
    
    def main(self):
        args = self.ArgumentsConfig()

        if(args.file):
            self.URLCheck(file = args.file)
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

    def URLCheck(self, file):
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

        #Mostrar dominios y paises
        print("Ejemplo de dominios:", cons.DOMINIO)
        print("Ejemplo de paises:", cons.PAIS)

        for line in lines:
            # Quitamos el /n al final del caracter
            line = line[:-1]

            #Hacemos un split con un punto.
            split = re.split(cons.SEPARADOR, line)

            correcto = False

            if (len(split) == 2):
                #Verificamos Https y Https
                correcto = VerificarProtocolo(cons = cons, split = split[0])

                #Verificamos dominio.
                if (correcto):
                    correcto = VerificarDominio(cons = cons, split = split[1])

            elif (len(split) == 1):
                correcto = VerificarDominio(cons = cons, split = split[0])

            if (correcto == True):
                print("La URL ingresada es correcto:", line)
            else:
                print("La URL ingresada es incorrecto:", line)

def VerificarDominio(cons, split):
    """Verifico si el dominio es correcto.

        args:
                -cons: Constantes.
                -split: Dominio en lista. 
    """
    split2 = re.split(cons.PUNTO, split)

    #Verificar www.----.com.ar
    if(len(split2) == 4):
        www = re.fullmatch(cons.WWW, split2[0])
        dom = re.fullmatch(cons.DOMINIO, split2[2])
        pais = re.fullmatch(cons.PAIS, split2[3])
        return (www and dom and pais) != None

    #Verificar www.---.com y ----.com.ar
    elif(len(split2) == 3):
        www = re.fullmatch(cons.WWW, split2[0])
        pais = re.fullmatch(cons.PAIS, split2[2])
        
        if (www != None):
            dom = re.fullmatch(cons.DOMINIO, split2[2])

            if (dom == None):
                dom = re.fullmatch(cons.DOMINIOBARRA, split2[2])

            return dom != None

        elif (pais != None):
            dom = re.fullmatch(cons.DOMINIO, split2[1])
            return dom != None
        
        else:
            return False

    #Verificar ---.com
    elif(len(split2) == 2):
        dom = re.fullmatch(cons.DOMINIO, split2[1])

        if (dom == None):
            dom = re.fullmatch(cons.DOMINIOBARRA, split2[1])

        return dom != None

    else:
        return False

    
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