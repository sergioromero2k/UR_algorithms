#!/usr/bin/env python3

def dfs_post(grafo, v, visited, resultado):
    visited.add(v)
    for nodo in grafo[v]:
        if nodo not in visited:
            dfs_post(grafo, nodo, visited, resultado)

    resultado.append(v)

def topological_sort(grafo):
    resultado = []
    visited = set()

    for v in range(1, len(grafo)):
        if v not in visited:
            dfs_post(grafo, v, visited, resultado)

    # El orden topológico es el post-orden inverso
    return resultado[::-1]

def main() -> None:
    # Grafo: Representación de adyacencia
    grafo = [
        [],         # 0
        [2, 4, 8],  # 1
        [3, 4],     # 2
        [5],        # 3
        [7],        # 4
        [6],        # 5
        [7],        # 6
        [9],        # 7
        [9],        # 8
        []          # 9
    ]

    print("Orden Topológico Correcto:")
    print(topological_sort(grafo))

if __name__ == "__main__":
    main()