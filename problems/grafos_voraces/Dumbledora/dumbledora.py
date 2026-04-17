#!/usr/bin/env python3

import heapq
import random

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
        hi, hj, c = map(int, input().strip().split())
        grafo[hi].append((hj, c))
        grafo[hj].append((hi, c))

    mst = prim(grafo, 0)

    coste_total = 0
    coste_habitacion = {i: 0 for i in range(n)}

    for (origen, nodo, peso) in mst:
        coste_total += peso
        coste_habitacion[origen] += peso
        coste_habitacion[nodo] += peso

    print(f"Coste total: {coste_total}")
    print("\n".join(f"H{i}: {coste_habitacion[i]}" for i in range(n)))


if __name__ == "__main__":
    main()

