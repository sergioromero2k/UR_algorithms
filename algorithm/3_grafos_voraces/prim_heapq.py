#!/usr/bin/env python3

import heapq

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