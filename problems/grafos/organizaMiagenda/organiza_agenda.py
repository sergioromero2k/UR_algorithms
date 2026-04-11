#!/usr/bin/env python3

import heapq

def main() -> None:
    n, r, t, m = input().strip().split()
    n, r = int(n), int(r)

    tipo_evento = {}
    marca_evento = {}

    for _ in range(n):
        i, x, y = input(). strip().split()
        i = int(i)
        tipo_evento[i] = x
        marca_evento[i] = y

    g = [[] for _ in range(n)]
    padres = [[] for _ in range(n)]

    n_aristas = [0] * n
    for _ in range(r):
        v, w = map(int, input().strip().split())
        g[v].append(w)
        padres[w].append(v)
        n_aristas[w] += 1

    prohibido = set()
    for i in range(n):
        if tipo_evento[i] == t and marca_evento[i] != m:
            prohibido.add(i)

    pq = [i for i in range(n) if n_aristas[i] == 0]
    heapq.heapify(pq)


    changed = True
    while changed:
        changed = False
        for i in range(n):
            if i not in prohibido and padres[i]:
                if all(p in prohibido for p in padres[i]):
                    prohibido.add(i)
                    changed = True

    pq = [i for i in range(n) if n_aristas[i] == 0]
    heapq.heapify(pq)

    resultado = []
    while pq:
        nodo_actual = heapq.heappop(pq)
        if nodo_actual not in prohibido:
            resultado.append(nodo_actual)
        for vecino in g[nodo_actual]:
            n_aristas[vecino] -= 1
            if n_aristas[vecino] == 0:
                heapq.heappush(pq, vecino)

    print(' '.join(marca_evento[i] for i in resultado))

if __name__ == "__main__":
    main()
