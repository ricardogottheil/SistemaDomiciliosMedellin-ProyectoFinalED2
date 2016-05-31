# -*- coding: utf-8 -*- 

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