# -*- coding: utf-8 -*- 

from Grafo import Arista, Grafo, agregar, caminoMinimo, construirCamino, dijkstra, generarEtiqueta, relacionar

def main():
    """ Funcion principal """

    grafo = Grafo()

    fn = open('Entrega2/vertices.txt', 'r')
    vertices = []
    coordx = []
    coordy = []
    nombres = []

    for line in fn:
        linea = line.split(',')
        vert = int(linea[0])
        coordenadax = linea[1]
        coordenaday = linea[2]
        nom = str(linea[3])
        

        vertices.append(vert)
        coordx.append(coordenadax)
        coordy.append(coordenaday)
        nombres.append(nom.rstrip('\n'))

    fn.close()

    print vertices
    print coordx
    print coordy
    print nombres



if __name__ == "__main__":
    main()