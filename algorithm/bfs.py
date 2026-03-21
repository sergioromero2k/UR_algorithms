"""
from collections import deque


def bfs_aux(v, g, visited):
    visited[v] = True
    print(v, end = " ")
    q = deque()
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True
                print(adj, end = " ")


def bfs(g):
    n = len(g)-1
    visited = [False] * (n+1)
    for v in range(1, n+1):
        if not visited[v]:
            bfs_aux(v, g, visited)



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

bfs(g)
"""

from collections import deque


def recorrido_bfs_desde_nodo(nodo_inicial, grafo, visitados):
    visitados[nodo_inicial] = True
    print(nodo_inicial, end=" ")

    cola = deque()
    cola.append(nodo_inicial)

    while cola:
        nodo_actual = cola.popleft()

        for vecino in grafo[nodo_actual]:
            if not visitados[vecino]:
                cola.append(vecino)
                visitados[vecino] = True
                print(vecino, end=" ")


def recorrido_bfs(grafo):
    """
    This BFS simply traverses the graph and prints the nodes in the order they are visited.
    It does not calculate shortest paths because it does not store parents or distances.
    The order 1 2 4 8 3 7 9 5 6 is simply the order in which BFS visits the nodes.
    """
    total_nodos = len(grafo) - 1
    visitados = [False] * (total_nodos + 1)

    for nodo in range(1, total_nodos + 1):
        if not visitados[nodo]:
            recorrido_bfs_desde_nodo(nodo, grafo, visitados)


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

recorrido_bfs(grafo)