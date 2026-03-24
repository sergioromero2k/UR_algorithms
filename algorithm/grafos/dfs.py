#!/urs/bin/env python3

def dfs_aux(nodo_actual, grafo, visited):
    visited.add(nodo_actual)
    for vecino in grafo[nodo_actual]:
        if vecino not in visited:
            dfs_aux(vecino, grafo, visited)


def dfs(grafo):
    visitado = set()

    for nodo in range(len(grafo)):
        if nodo not in visitado:
            dfs_aux(nodo, grafo,visitado)

grafo = [
    [],             # índice 0 no se usa
    [2, 4, 8],      # nodo 1 conectado a 2, 4, 8
    [1, 3, 4],      # nodo 2 conectado a 1, 3, 4
    [2, 4, 5],      # nodo 3 conectado a 2, 4, 5
    [1, 2, 3, 7],   # nodo 4 conectado a 1, 2, 3, 7
    [3, 6],         # nodo 5 conectado a 3, 6
    [5, 7],         # nodo 6 conectado a 5, 7
    [4, 6, 9],      # nodo 7 conectado a 4, 6, 9
    [1, 9],         # nodo 8 conectado a 1, 9
    [7, 8]          # nodo 9 conectado a 7, 8
]

dfs(grafo)




"""
def dfs_rec(v, g, visited):
    visited.add(v)
    print(f"Visiting node {v}")
    for u in g[v]:
        if u not in visited:
            dfs_rec(u, g, visited)


def dfs(g):
    n = len(g)-1
    visited = set()
    for v in range(1, n+1):
        if v not in visited:
            dfs_rec(v, g, visited)


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

dfs(g)
"""