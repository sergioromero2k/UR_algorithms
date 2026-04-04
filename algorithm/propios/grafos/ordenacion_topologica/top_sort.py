#!usr/bin/env python3

from collections import deque

def dfs(grafo, v, visitado, resultado):
    visitado.add(v)
    for vecino in grafo[v]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado, resultado)
    resultado.appendleft(v)

def topsort(grafo):
    resultado = deque()
    visitado = set()

    for prenda in grafo:
        if prenda not in visitado:
            dfs(grafo, prenda, visitado, resultado)
    return list(resultado)

def main() -> None:
    g = {
        "calcetines": ["zapatos"],
        "pantalon": ["zapatos", "cinturon"],
        "camisa": ["cinturon", "jersey"],
        "zapatos": [],
        "cinturon": [],
        "jersey": []
    }
    orden = topsort(g)
    print("Orden para vestirse:", orden)

if __name__ == "__main__":
    main()
