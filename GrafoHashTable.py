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

    def LecturaVertices(self, archivoTXT):
        """Lectura del archivoTXT para leer los datos y crear el grafo."""
        
        contenido = ''
        fh = open(archivoTXT)
        while True:
            line = fh.readline()
            contenido += line
            if line=='':
                break
        print(contenido)

    def LecturaArcos(self, archivoTXT):
        """Lectura del archivoTXT para leer los datos, para luego crear los arcos."""
        
        contenido = ''
        fh = open(archivoTXT)
        while True:
            line = fh.readline()
            contenido += line
            if line=='':
                break
        print(contenido)



    def getSize(self):
        """Devuelve el tamaño del grafo."""
        return self.size