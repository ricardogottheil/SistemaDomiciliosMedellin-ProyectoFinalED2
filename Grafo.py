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
        Método especial para que los obtetos como un string.
        """
        return str(self.relaciones)

class Arista(object):
    """"
    Clase Arista.
    """

    def __init__(self, elemento, peso):
        """
        Constructor de la clase Arista.
        """
        self.elemento = elemento
        self.peso = peso        
    def __str__(self):
        """
        Método especial para que los obtetos como un string.
        """
        return str(self.elemento) + str(self.peso)

 
def agregar(grafo, elemento):
    """
    Método para agregar un nodo al grafo.
    """
    grafo.relaciones.update({elemento:[]})

def relacionar(grafo, elemento1, elemento2, peso = 1):
    """
    Método para relacionar dos nodos. (Arcos)
    """
    relacionarUnilateral(grafo, elemento1, elemento2, peso)
    relacionarUnilateral(grafo, elemento2, elemento1, peso)
    
def relacionarUnilateral(grafo, origen, destino, peso):
    """
    Método para relacionar un nodo con otro. 
    """
    grafo.relaciones[origen].append(Arista(destino, peso))

def caminoMinimo(grafo, origen, destino):
    """
    Método para encontrar el camino entre dos nodos.
    """
    etiquetas = {origen:(0,None)}
    dijkstra(grafo, destino, etiquetas, [])
    return construirCamino(etiquetas, origen, destino)

def construirCamino(etiquetas, origen, destino):
    """
    Método para construir un camino entre dos nodos.
    """
    print origen, destino
    if origen == destino:
        return [origen]
    return construirCamino(etiquetas, origen, anterior(etiquetas[destino])) + [destino]
    
    
def dijkstra(grafo, destino, etiquetas, procesados):
    """
    Método para implementar el algoritmo de Djikstra.
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
    Método para generar las etiquetas.
    """
    etiquetaNodoAnterior = etiquetas[anterior]
    etiquetaPropuesta = peso(grafo, anterior, nodo) + acumulado(etiquetaNodoAnterior),anterior
    if (not(etiquetas.has_key(nodo)) or  acumulado(etiquetaPropuesta) < acumulado(etiquetas[nodo]) ):
        etiquetas.update({nodo:etiquetaPropuesta})

def aristas(grafo, nodo):
    """
    Método para retornar las aristas que tiene un nodo.
    """
    return grafo.relaciones[nodo]
        
def vecinoNoProcesado(grafo, nodo, procesados):
    """
    Método para retornar los vecino no procesados de un nodo
    """
    aristasDeVecinosNoProcesados = filter(lambda x: not x in procesados, aristas(grafo,nodo))
    return [arista.elemento for arista in aristasDeVecinosNoProcesados]


def peso(grafo, nodoOrigen, nodoDestino):
    """
    Método para retornar el peso de un nodo a otro
    """
    return reduce(lambda x,y: x if x.elemento == nodoDestino else y, grafo.relaciones[nodoOrigen]).peso 

def acumulado(etiqueta):
    """
    Método que retorna el acumulado.
    """
    return etiqueta[0]

def anterior(etiqueta):
    """
    Método que retorna la etiqueta anterior.
    """
    return etiqueta[1]
           
def menorValorNoProcesado(etiquetas, procesados):
    """
    Método que retorna el valor menor no procesado.
    """
    etiquetadosSinProcesar = filter(lambda (nodo,_):not nodo in procesados, etiquetas.iteritems())
    return min(etiquetadosSinProcesar, key=lambda (_, (acum, __)): acum)[0]

