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
        fh = open(archivoTXT, 'r')
        for linea in fh:
         print(linea)
        fh.close()


    def getSize(self):
        """Devuelve el tamaño del grafo."""
        return self.size