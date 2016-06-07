# -*- coding: utf-8 -*- 

from Grafo import Arista, Grafo, agregar, caminoMinimo, construirCamino, dijkstra, generarEtiqueta, relacionar

def main():
    """ Funcion principal """


    ##  EJEMPLO
    
    # a = "a"
    # b = "b"
    # c = "c"
    # d = "d"
    # e = "e"
    # f = "f" 
    # g = "g" 
    # h = "h"

    # grafo = Grafo()
    # agregar(grafo, a)
    # agregar(grafo, b)
    # agregar(grafo, c)
    # agregar(grafo, d)
    # agregar(grafo, e)
    # agregar(grafo, f)
    # agregar(grafo, g)
    # agregar(grafo, h)

    # relacionar(grafo, a, c, 1)
    # relacionar(grafo, a, b, 3)
    # relacionar(grafo, b, d, 1)
    # relacionar(grafo, b, g, 5)
    # relacionar(grafo, c, f, 5)
    # relacionar(grafo, c, d, 2)
    # relacionar(grafo, d, f, 2)
    # relacionar(grafo, d, e, 4)
    # relacionar(grafo, e, h, 1)
    # relacionar(grafo, e, g, 2)
    # relacionar(grafo, f, h, 3)

    # print caminoMinimo(grafo, e, a)

    # FIN EJEMPLO

    #SE CREA EL GRAFO
    grafo = Grafo()

    # VERTICE

    f1 = open('Entrega2/vertices.txt', 'r')
    vertices = []
    coordx = []
    coordy = []
    nombresVertices = []

    for line in f1:
        linea = line.split(',')
        vert = int(linea[0])
        coordenadax = linea[1]
        coordenaday = linea[2]
        nom = str(linea[3])


        vertices.append(vert)
        coordx.append(coordenadax)
        coordy.append(coordenaday)
        nombresVertices.append(nom.rstrip('\n'))

    f1.close()

    #IMPRIMIR
    # for v,cx,cy,n in zip(vertices,coordx,coordy,nombresVertices):
    #     print 'Vertice: %s \n Coordenada X: %s \n Coordenada Y: %s \n Nombre Vertice: %s \n \n' % (v,cx,cy,n)

    # AGREGRAR NODOS
    for v in vertices:
        agregar(grafo, v)  


    # ARCOS     

    f2 = open('Entrega2/arcos.txt', 'r')
    vertices1 = []
    vertices2 = []
    distancia = []
    nombreArcos = []
    for line in f2:
        linea = line.split(',')
        vert1 = int(linea[0])
        vert2 = int(linea[1])
        dist = int(linea[2])
        nomArcos = str(linea[3])

        vertices1.append(vert1)
        vertices2.append(vert2)
        distancia.append(dist)
        nombreArcos.append(nomArcos.rstrip('\n'))

    f2.close()

    #IMPRIMIR
    # for v1,v2,d,n in zip(vertices1,vertices2,distancia,nombreArcos):
    #     print 'Vertice 1: %s \n Vertice 2: %s \n Distancia: %s \n Nombre Arco: %s \n \n' % (v1,v2,d,n) 

    # AGREGRAR ARCOS
    for v1,v2,n in zip(vertices1,vertices2,nombreArcos):
        relacionar(grafo, v1, v2, n)

    print caminoMinimo(grafo, 0,4)

if __name__ == "__main__":
    main()