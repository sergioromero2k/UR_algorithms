#!/usr/bin/env python3

import sys
from collections import deque

input = sys.stdin.readline

def bfs_min(grafo, inicio, n):
    distancia = [-1] * n
    cola = deque()
    distancia[inicio] = 1
    cola.append(inicio)

    while cola:
        nodo_actual = cola.popleft()
        for nodo in grafo[nodo_actual]:
            if distancia[nodo] == -1:
                distancia[nodo] = distancia[nodo_actual] + 1
                cola.append(nodo)
    return distancia


def main():
    n, m, c = map(int, input().split())
    g = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    casos = []
    for _ in range(c):
        o, d, p = map(int, input().split())
        casos.append((o, d, p))

    cache = {}
    for o, d, p in casos:
        if o not in cache:
            cache[o] = bfs_min(g, o, n)

    output = []
    for o, d, p in casos:
        minimo = cache[o][d]
        if minimo == -1 or minimo > p:
            output.append("MON TOYA POR FAVOR")
        else:
            output.append(str(minimo))

    print('\n'.join(output))


if __name__ == "__main__":
    main()