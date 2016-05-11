# -*- coding: utf-8 -*- 

class GrafoHashTable:

    """Tabla que contiene los datos de los vertices."""
    vertices = {}

    """Tabla que contienes los arcos de los vertices."""
    grafo = {}

    """Cantidad de vertices en el grafo."""
    size = None

    def Lectura(self, archivoTXT):
        pass

    def getSize(self):
        return GrafoHashTable.size

class Vertice:
    """Clase vertice."""

    def __init__(self, posX, posY, nombre):
        self._posX = posX
        self._posY = posY
        self._nombre = nombre

    def getPosX(self):
        return self._posX

    def getPosY(self):
        return self._posY

    def getNombre(self):
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