#!/usr/bin/env python3

from collections import deque

def recorrido_bfs_desde_nodo(nodo_inicial, grafo, visitados, padre):
    visitados[nodo_inicial] = True

    cola = deque()
    cola.append(nodo_inicial)

    while cola:
        nodo_actual = cola.popleft()
        for vecino in grafo[nodo_actual]:
            if not visitados[vecino]:
                cola.append(vecino)
                visitados[vecino] = True
                padre[vecino] = nodo_actual


def bfs(inicio, destino, grafo):
    """
    If you want to find the shortest paths from a source node to any destination,
    you need to keep track of a parent array or distance array while performing a breadth-first search (BFS).
    """
    total_nodos = len(grafo) - 1
    visitados = [False] * (total_nodos + 1)
    padre = [-1] * (total_nodos+1)
    recorrido_bfs_desde_nodo(inicio, grafo, visitados, padre)

    camino = []
    while destino != -1:
        camino.append(destino)
        destino = padre[destino]

    camino.reverse()

    return camino

grafo = [
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

"""
When you perform a BFS starting from a source node, this algorithm already determines the shortest distance and the shortest path from that source to all reachable nodes.
The parent array simply allows you to reconstruct those shortest paths to any destination node you want.
It doesn't store all possible routes; it only stores the shortest path that was discovered first for each node.
"""
padre = bfs(1, 6, grafo)

print(padre)