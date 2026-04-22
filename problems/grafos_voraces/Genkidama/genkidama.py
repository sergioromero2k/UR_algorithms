#!/usr/bin/env python3

def select_min(candidates, visited):
    node = None
    weight = float("Inf")
    for i in range(len(candidates)):
        if not visited[i] and candidates[i] < weight:
            node = i
            weight = candidates[i]
    return node, weight

def prim(g, n):
    sol = 0
    visited = [False] * n
    candidates = [float("Inf")] * n
    padre = [-1] * n
    aristas_mst = []

    # Arrancamos desde nodo 0
    visited[0] = True
    for destino, peso in g[0]:
        if peso < candidates[destino]:
            candidates[destino] = peso
            padre[destino] = 0

    for _ in range(n - 1):
        next_node, cost = select_min(candidates, visited)

        if next_node is None:
            # No hay candidatos alcanzables: buscar nodo no visitado para nueva componente
            for i in range(n):
                if not visited[i]:
                    next_node = i
                    cost = 0  # no suma coste, solo arranca nueva componente
                    break
            if next_node is None:
                break
            # Arrancar desde este nodo nuevo sin sumar coste
            visited[next_node] = True
            for destino, peso in g[next_node]:
                if not visited[destino] and peso < candidates[destino]:
                    candidates[destino] = peso
                    padre[destino] = next_node
            continue

        visited[next_node] = True
        sol += cost
        aristas_mst.append((padre[next_node], next_node))

        for destino, peso in g[next_node]:
            if not visited[destino] and peso < candidates[destino]:
                candidates[destino] = peso
                padre[destino] = next_node

    return sol, aristas_mst

def main():
    N, M = map(int, input().split())

    g = [[] for _ in range(N)]
    for _ in range(M):
        c1, c2, w = map(int, input().split())
        g[c1].append((c2, w))
        g[c2].append((c1, w))

    coste, aristas_mst = prim(g, N)

    # Contar grado de cada nodo en el MST
    grado = [0] * N
    for u, v in aristas_mst:
        grado[u] += 1
        grado[v] += 1

    max_grado = max(grado)
    mejores = [i for i in range(N) if grado[i] == max_grado]

    print(coste)
    print(*mejores)

if __name__ == "__main__":
    main()