#!/usr/bin/env

def dfs_desde_nodo(nodo_actual, grafo, visitados, nivel):
    visitados.add(nodo_actual)
    print('-' * nivel, nodo_actual, sep='')

    for vecino in sorted(grafo[nodo_actual]): # Orden lexicográfico
        if vecino not in visitados:
            dfs_desde_nodo(vecino, grafo, visitados, nivel + 1)


def dfs(grafo):
    visitados = set()

    for nodo in range(len(grafo)):
        if nodo not in visitados:
            dfs_desde_nodo(nodo, grafo, visitados, 0)


def main() -> None:
    n, m = map(int, input().strip().split())
    grafo = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().strip().split())
        grafo[u].append(v)
        grafo[v].append(u)  # Grafo no dirigido

    dfs(grafo)


if __name__ == "__main__":
    main()
