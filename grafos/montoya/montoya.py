#!/usr/bin/env python3
from collections import deque

def bfs(grafo, origen):
    n = len(grafo)
    visitado = [False] * n
    distancias = [float('inf')] * n
    cola = deque()

    cola.append((origen, 0))
    visitado[origen] = True
    distancias[origen] = 1

    while cola:
        nodo, dist = cola.popleft()
        for vecino in grafo[nodo]:
            if not visitado[vecino]:
                visitado[vecino] = True
                distancias[vecino] = dist + 2
                cola.append((vecino, dist + 1))

    return distancias

def main() -> None:
    n, m, c = map(int, input().strip().split())

    list_ady = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().strip().split())
        list_ady[u].append(v)
        list_ady[v].append(u)

    # BFS desde cada nodo UNA sola vez
    distancias = [bfs(list_ady, i) for i in range(n)]

    salida = []
    for _ in range(c):
        o, d, p = map(int, input().strip().split())
        resultado = distancias[o][d]
        if resultado <= p:
            salida.append(str(resultado))
        else:
            salida.append("MON TOYA POR FAVOR")

    print("\n".join(salida))

if __name__ == "__main__":
    main()