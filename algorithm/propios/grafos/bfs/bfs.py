#!/usr/bin/env python3

from collections import deque

def bfs(grafo, inicio):
    # Grafo conexo
    marked = [False] * len(grafo)
    queue = deque([inicio])
    marked[inicio] = True
    recorrido = []

    while queue:
        v = queue.popleft()
        recorrido.append(v)
        for nodo in grafo[v]:
            if not marked[nodo]:
                marked[nodo] = True
                queue.append(nodo)
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

    print(bfs(g, 1))


if __name__ == "__main__":
    main()
