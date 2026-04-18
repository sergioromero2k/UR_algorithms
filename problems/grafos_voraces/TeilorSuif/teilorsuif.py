#!/usr/bin/env python3

import heapq

def prim(grafo, inicio):
    visitados = set([inicio])
    heap = [(peso, inicio, vecino) for vecino, peso in grafo[inicio]]
    mst = []

    heapq.heapify(heap)
    while heap:
        peso, origen, nodo = heapq.heappop(heap)

        if nodo in visitados:
            continue
        visitados.add(nodo)
        mst.append((origen ,nodo, peso))
        for vecino, peso in grafo[nodo]:
            if vecino not in visitados:
                heapq.heappush(heap, (peso, nodo, vecino))
    return mst


def main() -> None:
    n, m = map(int, input().strip().split())
    grafo = {i: [] for i in range(n)}
    for _ in range(m):
        c1, c2, f = map(int, input().strip().split())
        grafo[c1].append((c2, f))
        grafo[c2].append((c1, f))

    mst = prim(grafo, 0)

    coste_total = 0
    coste_habitacion = {i: 0 for i in range(n)}

    for origen, nodo, peso in mst:
        coste_total += peso
        coste_habitacion[origen] += peso
        coste_habitacion[nodo] += peso

    media = coste_total / (n-1)
    print(f"Fuerzas desplegadas: {coste_total}")
    print(" ".join(str(i) for i in range(n) if coste_habitacion[i] < media))


if __name__ == "__main__":
    main()
