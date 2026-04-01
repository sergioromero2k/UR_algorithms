#!/usr/bin/env python3

def dfs_post(grafo, v, visited, resultado):
    visited.add(v)
    for nodo in grafo[v]:
        if nodo not in visited:
            dfs_post(grafo, nodo, visited, resultado)
    resultado.append(v)

def dfs_top_sort(grafo, origen):
    resultado = []
    visited = set()

    dfs_post(grafo, origen, visited, resultado)

    for v in range(1, len(grafo)):
        if v not in visited:
            dfs_post(grafo, v, visited, resultado)

    return resultado[::-1]

def main() -> None:
    grafo = [
        [],  # 0 no se usa
        [2, 4, 8],  # 1 → 2, 4, 8
        [3, 4],  # 2 → 3, 4
        [5],  # 3 → 5
        [7],  # 4 → 7
        [6],  # 5 → 6
        [7],  # 6 → 7
        [9],  # 7 → 9
        [9],  # 8 → 9
        []  # 9 no apunta a nadie
    ]

    print(dfs_top_sort(grafo, origen=1))  # [1, 8, 2, 4, 3, 5, 6, 7, 9]
    print(dfs_top_sort(grafo, origen=3))  # [3, 5, 6, 7, 9, 1, 8, 2, 4]  ← empieza en 3

if __name__ == "__main__":
    main()
