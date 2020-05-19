from colorama import init, Fore
import csv
import json
import os
import time

"""
Versión usando POO (Programació Orientada a Objetos)
"""

class Elemento():
    def __init__(self, ruta):
        """ El constructor del objeto Elemento """
        # Definición e inicialización de atributos
        
        # Si la ruta no existe, entonces se lanza una excepción y no se crea el objeto
        if os.path.exists(ruta):
            self.nombre = ruta
        else:
            raise FileNotFoundError(f"La ruta {ruta} no existe!")
        self.tamanio = self.obtener_tamanio()
        self.fecha = self.obtener_fecha()
        self.nivel = 0
        self.indent = 2
        self.es_ultimo = False
    
    def obtener_fecha(self):
        """ Obtener la fecha del elemento """
        try:
            fecha = os.path.getmtime(self.nombre)
            fecha = time.ctime(fecha)
        except FileNotFoundError:
            fecha = ""
        except PermissionError:
            fecha = ""
        
        return fecha

    def obtener_tamanio(self):
        """ Obtiene el tamaño en bytes del elemento """
        if os.path.isfile(self.nombre):  # si es un archivo?
            tamanio = os.path.getsize(self.nombre)
        else: # es una carpeta
            tamanio = 0
        
        return tamanio
    
    def __str__(self, pre=""):
        """ Regresa la versión en str de Elemento """
        return  "{:10}  {:15}  {}{}".format(
            self.tamanio, self.fecha, pre, self.nombre)

    
class Archivo(Elemento):
    def __init__(self, ruta):
        """  Inicializando objeto Archivo """
        Elemento.__init__(self, ruta)
    
    def __str__(self):
        """ Regresa la versión en str de Archivo """
        pre = " " * self.indent * (self.nivel + 1)  # Para saber si se indenta o no
        if self.es_ultimo:
            pre += "└─"
        else:
            pre += "├─"
        nombre = self.nombre
        self.nombre = os.path.basename(self.nombre)
        cad = Elemento.__str__(self, pre)
        self.nombre = nombre

        return  cad

    
class Carpeta(Elemento):
    def __init__(self, ruta):
        """ Inicializando objeto Carpeta """
        Elemento.__init__(self, ruta)
        self.elementos = []
        self.total = 0
        
    def obtener_elementos(self):
        """
        Obtiene los elementos de la carpeta
        """
        # Obtener la lista de elemento de un carpeta
        try:
            nombres = os.listdir(self.nombre)
        except PermissionError:
            return
        
        # Agregando carpeta a la lista de nombres
        nombres = [os.path.join(self.nombre, nom) for nom in nombres]

        # Agregar los datos adicionales a cada elemento
        for nom in nombres:
            if os.path.isdir(nom):  # Si nom es una carpeta?
                self.elementos.append(Carpeta(nom))
            else:
                archivo = Archivo(nom)
                self.elementos.append(archivo)
                self.tamanio += archivo.tamanio

        # Se obtiene el total de la carpeta, inicialmente es igual a tamanio 
        self.total = self.tamanio

    def __str__(self):
        """ Regresa la versión en str de Carpeta """
        pre = " " * self.indent * self.nivel  # Para saber si se indenta o no
        pre += "" if not self.nivel else "└─"
        nombre = self.nombre
        self.nombre = os.path.basename(self.nombre)
        cad = Elemento.__str__(self, pre) + os.path.sep
        self.nombre = nombre

        return cad

        
def imprimir_elementos(carpeta, nivel=0):
    """
    Imprime la lista de elementos en formato texto en la salida
    estándar de carpeta.
    """
    init(autoreset=True)
    carpeta.nivel = nivel
    print(Fore.GREEN + str(carpeta))
    for e in carpeta.elementos:
        if isinstance(e, Carpeta):
            e.obtener_elementos()
            imprimir_elementos(e, nivel+1)
        else:
            e.nivel = nivel
            if e == carpeta.elementos[-1]:
                e.es_ultimo = True
            print(e)

def guardar_elementos(elementos):
    """
    Guarda la lista de elementos en el archivo salida.txt.
    """
    archivo = "salida.txt"
    
    da = open(archivo, "w")
    # Imprimir la lista
    da.write("-" * 80 + "\n")
    for e in elementos:  # e = ["nom", 1234, "fecha"]
        # print("{} {}".format(e[0], e[1])
        if os.path.isdir(e[0]): # e = ["nom/", 1234, "fecha"]
            e[0] += "/" # e[0] = e[0] + "/"
        print("{:10} | {:15} | {}".format(*e), file=da)
    print("-" * 80, file=da)
    
    da.close()

def guardar_elementos_csv(elementos):
    """
    Guarda la lista de elementos en el archivo salida.csv.
    """
    archivo = "salida.csv"
    
    with open(archivo, "w") as da:
        # Crear un descript de archivo en csv
        da_csv = csv.writer(da)
        # Guarda el encabezado
        enc = ["Tamaño", "Fecha","Nombre"]
        da_csv.writerow(enc)
        # Guardar la lista
        for e in elementos:  # e = [1234,"fecha","nom"]
            # print("{} {}".format(e[0], e[1])
            if os.path.isdir(e[2]): # e = [1234, "fecha","nom/"]
                e[2] += "/" # e[3] = e[3] + "/"
            da_csv.writerow(e)

def guardar_elementos_json(elementos):
    """
    Guarda la lista de elementos en el archivo salida.json.
    """
    archivo = "salida.json"
    
    with open(archivo, "w") as da:
        json.dump(elementos, da, indent=4)

# MVC: Controlador
def main():
    """ Es la función principal del script o módulo """
    # Variables
    ruta = "."  # Carpeta actual

    # Instanciar objetos
    carpeta = Carpeta(ruta)  # carpeta es de tipo Carpeta()
    carpeta.obtener_elementos()
    
    imprimir_elementos(carpeta)
    # guardar_elementos(carpeta.elementos)
    # guardar_elementos_csv(carpeta.elementos)
    # guardar_elementos_json(carpeta.elementos)

# Para poder ejecutarlo como módulo
if __name__ == "__main__": 
    main()