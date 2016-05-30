# -*- coding: utf-8 -*- 

class GrafoHashTable:
    """Clase GrafoHashTable"""
    
    def __init__(self):
        """
            Constructor de la clase GrafoHashTable con la declaracion de los vertices, del grafo y el size.

            Vertices: Tabla que contiene los datos de los vertices.
            Grafo: Tabla que contienes los arcos de los vertices.
            Size: Cantidad de vertices en el grafo.
        """
        self.vertices = {}
        self.grafo = {}
        self.size = None

    def Lectura(self, archivoTXT):
        """Lectura del archivoTXT para leer los datos y crear el grafo."""
        self.archivo = archivoTXT
        fh = open(self.archivo, 'r')
        for linea in fh:
         print(linea)
        fh.close()


    def getSize(self):
        """Devuelve el tamaño del grafo."""
        return self.size

class Vertice:
    """Clase vertice."""

    def __init__(self, posX, posY, nombre):
        self._posX = posX
        self._posY = posY
        self._nombre = nombre

    def getPosX(self):
        """Devuelve la posicion x del vertice."""
        return self._posX

    def getPosY(self):
        """Devuelve la posicion y del vertice."""
        return self._posY

    def getNombre(self):
        """Devuelve el nombre del vertice."""
        return self._nombre

class Arco:
    """Clase para crear el arco con su respectivo nombre y distancia.""" 
    
    def __init__(self, nombre, distancia):
        """Constructor para definir la distancia y el nombre del arco"""
        self._nombre = nombre
        self._distancia = distancia

    def getNombre(self):
        """Método que retorna el nombre del arco."""
        return self._nombre

    def getDistancia(self):
        """Método que retorna la distancia del arco"""
        return self._distancia

def main():
    """ Funcion main """
    # 'Ejemplo-entrada-salida-entrega2/archivo-entrada-ejemplo.txt'
    # fh = open('Ejemplo-entrada-salida-entrega2/archivo-entrada-ejemplo.txt', 'r')
    # for linea in fh:
    #  print(linea)
    # fh.close()
    # 
    GrafoHashTable.Lectura('Ejemplo-entrada-salida-entrega2/archivo-entrada-ejemplo.txt')


if __name__ == "__main__":
    main()