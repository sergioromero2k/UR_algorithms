#!/usr/bin/env python3

from collections import deque

def dfs(grafo, origen, visited, resultado):
    cola = deque()

    visited.add(origen)
    cola.append(origen)

    while cola:
        nodo_actual = cola.popleft()
        resultado.append(nodo_actual)
        for nodo in grafo[nodo_actual]:
            if nodo not in visited:
                visited.add(nodo)
                cola.append(nodo)
    return resultado

def dfs_completo(grafo, origen):
    # Grafo no conexo
    visited = set()
    recorrido = []

    dfs(grafo, origen, visited, recorrido)
    for v in range(1, len(grafo)):
        if v not in visited:
            dfs(grafo, v, visited, recorrido)

    return recorrido

def main() -> None:
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

    print(dfs_completo(g, 1))


if __name__ == "__main__":
    main()
