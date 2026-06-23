""" OLD
from collections import deque

def topsort(g):
    data = {
        "graph": g,
        "state": dict(),
        "d": dict(),
        "f": dict(),
        "time": 0,
        "list": deque()
    }
    for k in g.keys():
        data['state'][k] = 'NOT_VISITED'
        data['d'][k] = 0
        data['f'][k] = 0

    for k in g.keys():
        if data['state'][k] == "NOT_VISITED":
            top_sort_visit(data, k)
    print(data['list'])

def top_sort_visit(data, k):
    data['state'][k] = "VISITED"
    data['time'] += 1
    data['d'][k] = data['time']
    for adj in data['graph'][k]:
        if data['state'][adj] == "NOT_VISITED":
            top_sort_visit(data, adj)
    data['state'][k] = 'FINISHED'
    data['time'] += 1
    data['f'][k] = data['time']
    data['list'].appendleft(k)




g = {
    "calcetines": ["zapatos"],
    "pantalon": ["zapatos", "cinturon"],
    "camisa": ["cinturon", "jersey"],
    "zapatos": [],
    "cinturon": [],
    "jersey": []
}

topsort(g)
"""

""" BEST
Qué hace: ordena nodos respetando dependencias.

Cuándo usarlo:
    "orden de tareas con dependencias"
    "prerequisitos de asignaturas"
    "orden de compilación de archivos"
    "ponerse la ropa"
    "antes de X hay que hacer Y"
"""
from collections import deque

def dfs_rec(g, v, visited, result):
    visited.add(v)
    for adj in g[v]:
        if adj not in visited:
            dfs_rec(g, adj, visited, result)
    result.appendleft(v)  # única línea nueva

def topsort(g):
    visited = set()
    result = deque()
    for v in g:
        if v not in visited:
            dfs_rec(g, v, visited, result)
    print(list(result))

g = {
    "calcetines": ["zapatos"],
    "pantalon": ["zapatos", "cinturon"],
    "camisa": ["cinturon", "jersey"],
    "zapatos": [], "cinturon": [], "jersey": []
}
topsort(g)