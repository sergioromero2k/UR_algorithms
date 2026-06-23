"""OLD
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

""" BEST
* Este es mejor y mucho mas entendible...
* El art_points encuentra nodos cuya eliminación desconecta el grafo.

Cuándo usarlo:
    "punto crítico de la red"
    "si falla este nodo, la red se desconecta"
    "vulnerabilidad en una red"
    "nodo más importante"
    "puente en una red de comunicaciones"

        n    → número de nodos
        disc → discovery time, tiempo en que se descubre cada nodo (-1 = no visitado)
        low  → lowest discovery time, mínimo tiempo alcanzable desde cada nodo
        ap   → articulation points, True si el nodo es punto de articulación
        time → contador global de tiempo (lista para poder modificarlo en dfs interno)
"""

def findArticulationPoints(g):
    n = len(g)
    disc = [-1] * n
    low = [-1] * n
    ap = [False] * n
    time = [0]

    def dfs(u, parent):
        disc[u] = low[u] = time[0]
        time[0] += 1
        children = 0
        for v in g[u]:
            if disc[v] == -1:
                children += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if parent != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent:
                low[u] = min(low[u], disc[v])
        if parent == -1 and children > 1:
            ap[u] = True

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
    return [i for i in range(n) if ap[i]]

g = [[1,2,3],[0,2,4,5],[0,1,5],[0,6,7],[1,5],[1,2,4],[3,7],[3,6]]
print(findArticulationPoints(g))