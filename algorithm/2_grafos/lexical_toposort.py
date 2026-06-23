#!/usr/bin/env python3

def lexic_top_sort(g, n):
    aristas_entrantes = [0] * n
    for u in range(n):
        for v in g[u]:
            aristas_entrantes[v] += 1

    nodos_iniciales = []
    for i in range(n):
        if aristas_entrantes[i] == 0:
            nodos_iniciales.append(i)

    resultado = []
    ciclos = 0
    while nodos_iniciales:
        nodos_iniciales.sort()
        origen = nodos_iniciales.pop(0)
        resultado.append(origen)
        for nodo in g[origen]:
            aristas_entrantes[nodo] -= 1
            if aristas_entrantes[nodo] == 0:
                nodos_iniciales.append(nodo)
        ciclos += 1

    if ciclos != n:
        print(-1)
        return
    for tarea in resultado:
        print(tarea, end=' ')

def main() -> None:
    n, m = map(int, input().strip().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        orig, dest = map(int, input().strip().split())
        g[orig].append(dest)
    lexic_top_sort(g, n)


if __name__ == "__main__":
    main()
