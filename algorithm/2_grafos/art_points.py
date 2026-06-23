#!/usr/bin/env python3

def dfs(grafo, tiempo_desc, low, padre, tiempo, es_articulacion, nodo):
    tiempo_desc[nodo] = tiempo[0]
    low[nodo] = tiempo[0]
    tiempo[0] += 1

    hijos = 0

    for vecino in grafo[nodo]:
        if tiempo_desc[vecino] == -1:
            padre[vecino] = nodo
            hijos += 1

            dfs(grafo, tiempo_desc, low, padre, tiempo, es_articulacion, vecino)

            low[nodo] = min(low[nodo], low[vecino])

            if padre[nodo] != -1 and low[vecino] >= tiempo_desc[nodo]:
                es_articulacion[nodo] = True

        elif vecino != padre[nodo]:
            low[nodo] = min(low[nodo], tiempo_desc[vecino])

    if padre[nodo] == -1 and hijos > 1:
        es_articulacion[nodo] = True

def encontrar_puntos_articulacion(grafo):
    n = len(grafo)

    tiempo_desc = [-1] * n
    low = [-1] * n
    padre = [-1] * n
    es_articulacion = [False] * n

    tiempo = [0]

    for nodo in range(n):
        if tiempo_desc[nodo] == -1:
            dfs(grafo, tiempo_desc, low, padre, tiempo, es_articulacion, nodo)

    return [i for i in range(n) if es_articulacion[i]]

grafo = [
    [1, 2, 3],
    [0, 2, 4, 5],
    [0, 1, 5],
    [0, 6, 7],
    [1, 5],
    [1, 2, 4],
    [3, 7],
    [3, 6]
]

print(encontrar_puntos_articulacion(grafo))



"""
def dfs(g, disc, low, parent, time, ap, u):
    disc[u] = time[0]
    low[u] = time[0]
    time[0] += 1
    children = 0
    for v in g[u]:
        if disc[v] == -1:
            parent[v] = u
            children += 1
            dfs(g, disc, low, parent, time, ap, v)
            low[u] = min(low[u], low[v])
            if parent[u] != -1 and low[v] >= disc[u]:
                ap[u] = True
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])
    if parent[u] == -1 and children > 1:
        ap[u] = True

def findArticulationPoints(g):
    v = len(g)
    disc = [-1] * v
    low = [-1] * v
    parent = [-1] * v
    ap = [False] * v
    time = [1]
    for i in range(v):
        if disc[i] == -1:
            dfs(g, disc, low, parent, time, ap, i)
    art_points = [node for node in range(v) if ap[node]]
    return art_points

g = [[1,2,3], [0,2,4,5], [0,1,5], [0, 6, 7], [1, 5], [1,2, 4], [3, 7], [3, 6]]

print(findArticulationPoints(g))
"""