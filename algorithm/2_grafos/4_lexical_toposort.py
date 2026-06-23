""" OLD
lexical_toposort

def lexic_top_sort(g, n):
    aristas_entrantes = [0] * n
    for u in range(n):
        for v in g[u]:
            aristas_entrantes[v] += 1

    nodos_iniciales = []
    for i in range(n):
        if aristas_entrantes[i] == 0:
            nodos_iniciales.append(i)
    topological_sort = []
    cnt = 0
    while nodos_iniciales:
        nodos_iniciales.sort()
        origen = nodos_iniciales.pop(0)
        topological_sort.append(origen)
        for adj in g[origen]:
            aristas_entrantes[adj] -= 1
            if aristas_entrantes[adj] == 0:
                nodos_iniciales.append(adj)
        cnt += 1
    if cnt != n:
        print(-1)
        return
    for tarea in topological_sort:
        print(tarea, end=' ')

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        orig, dest = map(int, input().strip().split())
        g[orig].append(dest)
    lexic_top_sort(g, n)
"""

"""BEST
Lexical Topsort

Qué hace: igual que topsort pero el resultado es lexicográficamente el menor posible.
* Lexicograficamente = Es ordenar como en un diccionario, por orden alfabético o numérico.
EJM:

g:
0 → 2
1 → 2
2 → 3

# En topsort hay varios órdenes válidos, el lexicográfico es el más pequeño posible:
Órdenes válidos:
[0, 1, 2, 3]  ← lexicográfico (el menor)
[1, 0, 2, 3]  ← también válido pero no es el menor

Cuándo usarlo:
    "orden topológico lexicográfico"
    "menor orden posible"
    "nodos son números"
    "detectar ciclo en grafo dirigido"
"""
import heapq

def lexic_topsort(g, n):
    entrantes = [0] * n
    for u in range(n):
        for v in g[u]:
            entrantes[v] += 1
    heap = [i for i in range(n) if entrantes[i] == 0]
    heapq.heapify(heap)
    result = []
    while heap:
        u = heapq.heappop(heap)
        result.append(u)
        for v in g[u]:
            entrantes[v] -= 1
            if entrantes[v] == 0:
                heapq.heappush(heap, v)
    print(*result if len(result) == n else [-1])