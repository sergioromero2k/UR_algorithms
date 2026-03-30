from collections import deque


def visitar_nodo(contexto, nodo_actual):
    contexto["estado"][nodo_actual] = "VISITED"
    contexto["tiempo_actual"] += 1
    contexto["tiempo_entrada"][nodo_actual] = contexto["tiempo_actual"]

    for nodo_vecino in contexto["grafo"][nodo_actual]:
        if contexto["estado"][nodo_vecino] == "NOT_VISITED":
            visitar_nodo(contexto, nodo_vecino)

    contexto["estado"][nodo_actual] = "FINISHED"
    contexto["tiempo_actual"] += 1
    contexto["tiempo_salida"][nodo_actual] = contexto["tiempo_actual"]
    contexto["resultado"].appendleft(nodo_actual)


def ordenacion_topologica(grafo):
    contexto = {
        "grafo": grafo,
        "estado": dict(),
        "tiempo_entrada": dict(),
        "tiempo_salida": dict(),
        "tiempo_actual": 0,
        "resultado": deque()
    }

    for nodo in grafo.keys():
        contexto["estado"][nodo] = "NOT_VISITED"
        contexto["tiempo_entrada"][nodo] = 0
        contexto["tiempo_salida"][nodo] = 0

    for nodo in grafo.keys():
        if contexto["estado"][nodo] == "NOT_VISITED":
            visitar_nodo(contexto, nodo)

    print(contexto["resultado"])


def main() -> None:
    grafo_ropa = {
        "calcetines": ["zapatos"],
        "pantalon": ["zapatos", "cinturon"],
        "camisa": ["cinturon", "jersey"],
        "zapatos": [],
        "cinturon": [],
        "jersey": []
    }

    ordenacion_topologica(grafo_ropa)

if __name__ == "__main__":
    main()







"""
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

def main() -> None:
    g = {
        "calcetines": ["zapatos"],
        "pantalon": ["zapatos", "cinturon"],
        "camisa": ["cinturon", "jersey"],
        "zapatos": [],
        "cinturon": [],
        "jersey": []
    }

    topsort(g)

if __name__ == "__main__":
    main()
"""