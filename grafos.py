# -*- coding: utf-8 -*- 

class GrafoHashTable:
    """Clase GrafoHashTable"""

    vertices = {}
    """Tabla que contiene los datos de los vertices."""

    grafo = {}
    """Tabla que contienes los arcos de los vertices."""

    size = None
    """Cantidad de vertices en el grafo."""

    def Lectura(self, archivoTXT):
        """Lectura del archivoTXT para leer los datos."""
        pass

    def getSize(self):
        """Devuelve el tamaño del grafo."""
        return GrafoHashTable.size

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