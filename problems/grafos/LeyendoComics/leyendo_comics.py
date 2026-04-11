#!/usr/bin/env python3

import heapq

def lexical_topsort(grafo, n):
    n_aristas = [0] * n
    for u in range(n):
        for v in grafo[u]:
            n_aristas[v] += 1

    pq = [nodo for nodo in range(n) if n_aristas[nodo] == 0]
    heapq.heapify(pq)

    resultado = []
    while pq:
        nodo_actual = heapq.heappop(pq)
        resultado.append(nodo_actual)
        for vecino in grafo[nodo_actual]:
            n_aristas[vecino] -= 1
            if n_aristas[vecino] == 0:
                heapq.heappush(pq, vecino)

    return list(resultado)



def main() -> None:
    n, m = map(int, input().strip().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().strip().split())
        g[a].append(b)

    lexical = lexical_topsort(g, len(g))
    resultado = " ".join(map(str, lexical))
    print(resultado)

if __name__ == "__main__":
    main()
