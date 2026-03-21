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

def bfs(inicio, grafo):
    total_nodos = len(grafo) - 1
    visitados = [False] * (total_nodos + 1)
    padre = [-1] * (total_nodos + 1)
    recorrido_bfs_desde_nodo(inicio, grafo, visitados, padre)

    return padre


def main():
    n, m = map(int, input().strip().split())
    maze = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        maze.append(row)

    paso = 1
    for i  in range(n):
        for j in range(m):
            ...




if __name__ == "__main__":
    main()