# -*- coding: utf-8 -*- 

"""
Implementación del grafo.
"""
class Grafo(object):
    """"
    Clase Grafo
    """

    def __init__(self):
        """
        Contructor de la clase Grafo.
        """
        self.relaciones = {}
    def __str__(self):
        """
        Metodo especial para que los obtetos como un string.
        """
        return str(self.relaciones)

    # def hamiltoniano(self, current=None, pending=None, destiny=None):
    #     if pending is None:
    #         pending = self.relaciones.values()

    #     result = None

    #     if current is None:
    #         for current in pending:
    #             result = self.hamiltoniano(current, [x for x in pending if x is not current], current)
    #             if result is not None:
    #                 break
    #     else:
    #         if pending == []: 
    #             if current.reaches(destiny):
    #                 return [current]
    #             else:
    #                 return None
 
    #         for x in [self.relaciones[v] for v in current.peso]:
    #             if x in pending:
    #                 result = self.hamiltoniano(x, [y for y in pending if y is not x], destiny)
    #                 if result is not None:
    #                     result = [current] + result
    #                     break    
 
    #     return result

class Arista(object):
    """"
    Clase Arista.
    """

    def __init__(self, elemento, peso):
        """
        Constructor de la clase Arista.

        :type elemento: grafo
        :param elemento: Elemento

        :type peso: int
        :param peso: Peso de la arista    

        """
        self.elemento = elemento
        self.peso = peso        
    def __str__(self):
        """
        Metodo especial para que los obtetos como un string.
        """
        return str(self.elemento) + str(self.peso)

 
def agregar(grafo, elemento):
    """
    Metodo para agregar un nodo al grafo.

    :type grafo: grafo
    :param grafo: Objeto grafo

    :type elemento: Variable
    :param elemento: Elemento a agregar al grafo 
    """
    grafo.relaciones.update({elemento:[]})

def relacionar(grafo, elemento1, elemento2, peso = 1):
    """
    Metodo para relacionar dos nodos. (Arcos)
    
    :type grafo: grafo
    :param grafo: Objeto grafo

    :type elemento1: Variable
    :param elemento1: Elemento 1 a relacionar con el elemento 2 

    :type elemento2: Variable
    :param elemento2: Elemento 2 a relacionar con el elemento 1

    :type peso: int 
    :param peso: Peso de la relación

    """
    relacionarUnilateral(grafo, elemento1, elemento2, peso)
    relacionarUnilateral(grafo, elemento2, elemento1, peso)
    
def relacionarUnilateral(grafo, origen, destino, peso):
    """
    Metodo para relacionar un nodo con otro.

    :type grafo: grafo
    :param grafo: Objeto grafo

    :type origen: Variable
    :param origen: Nodo origen

    :type destino: Variable
    :param destino: Nodo destino

    :type peso: int 
    :param peso: Peso de la relación

    """
    grafo.relaciones[origen].append(Arista(destino, peso))

def caminoMinimo(grafo, origen, destino):
    """
    Metodo para encontrar el camino entre dos nodos.

    :type grafo: grafo
    :param grafo: Objeto grafo

    :type origen: Variable
    :param origen: Nodo origen

    :type destino: Variable
    :param destino: Nodo destino
    """
    etiquetas = {origen:(0,None)}
    dijkstra(grafo, destino, etiquetas, [])
    return construirCamino(etiquetas, origen, destino)

def construirCamino(etiquetas, origen, destino):
    """
    Metodo para construir un camino entre dos nodos.

    :type grafo: grafo
    :param grafo: Objeto grafo

    :type origen: Variable
    :param origen: Nodo origen

    :type destino: Variable
    :param destino: Nodo destino
    """
    print origen, destino
    if origen == destino:
        return [origen]
    return construirCamino(etiquetas, origen, anterior(etiquetas[destino])) + [destino]
    
    
def dijkstra(grafo, destino, etiquetas, procesados):
    """
    Metodo para implementar el algoritmo de Djikstra.

    :type grafo: grafo
    :param grafo: Objeto grafo

    :type destino: Variable
    :param destino: Nodo destino

    :type etiquetas: string
    :param etiquetas: Nombre de cada nodo

    :type procesados: Variable
    :param procesados: Elementos procesados del grafo
    """
    nodoActual = menorValorNoProcesado(etiquetas, procesados)
    if nodoActual == destino: 
        return
    procesados.append(nodoActual)
    for vecino in vecinoNoProcesado(grafo, nodoActual, procesados):
        generarEtiqueta(grafo, vecino, nodoActual, etiquetas)
    dijkstra(grafo, destino, etiquetas, procesados)


def generarEtiqueta(grafo, nodo, anterior, etiquetas):
    """
    Metodo para generar las etiquetas.

    :type grafo: grafo
    :param grafo: Objeto grafo

    :type nodo: Variable
    :param nodo: Nodo del grafo

    :type anterior: array
    :param anterior: Etiqueta anterior

    :type etiquetas: string
    :param etiquetas: Nombre de cada nodo

    """
    etiquetaNodoAnterior = etiquetas[anterior]
    etiquetaPropuesta = peso(grafo, anterior, nodo) + acumulado(etiquetaNodoAnterior),anterior
    if (not(etiquetas.has_key(nodo)) or  acumulado(etiquetaPropuesta) < acumulado(etiquetas[nodo]) ):
        etiquetas.update({nodo:etiquetaPropuesta})

def aristas(grafo, nodo):
    """
    Metodo para retornar las aristas que tiene un nodo.

    :type grafo: grafo
    :param grafo: Objeto grafo

    :type nodo: Variable
    :param nodo: Nodo del grafo
    """
    return grafo.relaciones[nodo]
        
def vecinoNoProcesado(grafo, nodo, procesados):
    """
    Metodo para retornar los vecino no procesados de un nodo

    :type grafo: grafo
    :param grafo: Objeto grafo

    :type nodo: Variable
    :param nodo: Nodo del grafo

    :type procesados: Variable
    :param procesados: Elementos procesados del grafo
    """
    aristasDeVecinosNoProcesados = filter(lambda x: not x in procesados, aristas(grafo,nodo))
    return [arista.elemento for arista in aristasDeVecinosNoProcesados]


def peso(grafo, nodoOrigen, nodoDestino):
    """
    Metodo para retornar el peso de un nodo a otro

    :type nodoOrigen: Variable
    :param nodoOrigen: Nodo origen

    :type nodoDestino: Variable
    :param nodoDestino: Nodo destino
    """
    return reduce(lambda x,y: x if x.elemento == nodoDestino else y, grafo.relaciones[nodoOrigen]).peso 

def acumulado(etiqueta):
    """
    Metodo que retorna el acumulado.

    :type etiqueta: string
    :param etiqueta: Nombre de cada nodo
    """
    return etiqueta[0]

def anterior(etiqueta):
    """
    Metodo que retorna la etiqueta anterior.

    :type etiqueta: string
    :param etiqueta: Nombre de cada nodo
    """
    return etiqueta[1]
           
def menorValorNoProcesado(etiquetas, procesados):
    """
    Metodo que retorna el valor menor no procesado.

    :type etiquetas: string
    :param etiquetas: Nombre de cada nodo
    
    :type procesados: Variable
    :param procesados: Elementos procesados del grafo
    """
    etiquetadosSinProcesar = filter(lambda (nodo,_):not nodo in procesados, etiquetas.iteritems())
    return min(etiquetadosSinProcesar, key=lambda (_, (acum, __)): acum)[0]

