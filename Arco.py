# -*- coding: utf-8 -*- 

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