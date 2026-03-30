#!/usr/bin/env python3


def dfs_aux(grafo, v, visited, preferencia, p):
    visited.add(v)
    for vecino in grafo[v]:
        if vecino not in visited and preferencia[vecino] == p:
            dfs_aux(grafo, vecino, visited, preferencia, p)

def dfs(grafo, preferencia, p):
    n = len(grafo)
    visited = set()
    salas = 0
    for v in range(n):
        if v not in visited and preferencia[v] == p:
            dfs_aux(grafo, v, visited, preferencia, p)
            salas += 1
    print(salas)

def main() -> None:
    n, m, p = input().strip().split()
    n = int(n)
    m = int(m)

    lista_adyac = [[] for _ in range(n)]
    preferencias = []

    for _ in range(n):
        preferencias.append(input().strip())

    for i in range(m):
        a, b = map(int, input().strip().split())
        lista_adyac[a].append(b)
        lista_adyac[b].append(a)

    dfs(lista_adyac, preferencias, p)

if __name__ == "__main__":
    main()
