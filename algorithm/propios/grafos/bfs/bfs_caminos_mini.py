#!/usr/bin/env python3

from collections import deque


def bfs_camino_minimo(grafo, origen, destino):
    """
    Calcula el camino mínimo entre origen y destino usando BFS.

    BFS garantiza el camino más corto porque explora nivel a nivel.
    Guarda el padre de cada nodo para reconstruir el camino al final.

    Args:
        grafo: lista de adyacencia
        origen: nodo de inicio
        destino: nodo al que queremos llegar

    Returns:
        camino: lista de nodos del camino más corto
        distancia: número de saltos
    """
    visited = set()
    cola = deque()
    padre = {}
    distancia = {}

    visited.add(origen)
    cola.append(origen)
    padre[origen] = None
    distancia[origen] = 0

    while cola:
        nodo_actual = cola.popleft()

        if nodo_actual == destino:
            break

        for nodo in grafo[nodo_actual]:
            if nodo not in visited:
                visited.add(nodo)
                cola.append(nodo)
                padre[nodo] = nodo_actual
                distancia[nodo] = distancia[nodo_actual] + 1

    camino = []
    nodo = destino

    while nodo is not None:
        camino.append(nodo)
        nodo = padre[nodo]

    camino.reverse()
    return camino, distancia[destino]



def main() ->None:

    g = [
        [],
        [2, 4, 8],
        [1, 3, 4],
        [2, 4, 5],
        [1, 2, 3, 7],
        [3, 6],
        [5, 7],
        [4, 6, 9],
        [1, 9],
        [7, 8]
    ]

    camino, dist = bfs_camino_minimo(g, 1, 6)
    print(f"Camino: {camino}")
    print(f"Distancia: {dist}")

if __name__ == "__main__":
    main()
