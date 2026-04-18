#!/usr/bin/env python3

import heapq
import math

def prim(grafo, inicio):
    visitados = set([inicio])
    heap = [(peso, inicio, vecino) for vecino, peso in grafo[inicio]]
    heapq.heapify(heap)
    mst = []

    while heap:
        peso, origen, nodo = heapq.heappop(heap)
        if nodo in visitados:
            continue
        visitados.add(nodo)
        mst.append((origen, nodo, peso))
        for vecino, p in grafo[nodo]:
            if vecino not in visitados:
                heapq.heappush(heap, (p, nodo, vecino))

    return mst

def main() -> None:
    n, m = map(int, input().strip().split())

    grafo = {i: [] for i in range(n)}
    for _ in range(m):
        n1, n2, d = map(int, input().strip().split())
        grafo[n1].append((n2, d))
        grafo[n2].append((n1, d))

    mst = prim(grafo, 0)

    coste_total = 0

    for (origen, nodo, peso) in mst:
        coste_total += peso

    coste = math.ceil(coste_total/5)
    print(coste)

if __name__ == "__main__":
    main()
