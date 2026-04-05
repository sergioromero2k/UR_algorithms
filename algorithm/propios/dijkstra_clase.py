#!/usr/bin/env python3

def select_min(distancia, visited):
    vecino = 0
    min_dist = 0x3f3f3f3f
    for i in range(1, len(distancia)):
        if not visited[i] and distancia[i] < min_dist:
            vecino = i
            min_dist = distancia[i]
    return vecino


def dijkstra(grafo, inicio):
    n = len(grafo)-1
    distancia = [0x3f3f3f3f] * (n+1)
    visited = [False] * (n+1)

    distancia[inicio] = 0
    visited[inicio] = True

    for src, dst, w in grafo[inicio]:
        distancia[dst] = w

    for _ in range(2, n+1):
        vecino = select_min(distancia, visited)
        visited[vecino] = True
        for src, dst, w in grafo[vecino]:
            distancia[dst] = min(distancia[dst], distancia[src]+w)

    return distancia



def main() -> None:
    g = [
        [],
        [(1, 2, 5), (1, 4, 3)],
        [(2, 5, 1)],
        [],
        [(4, 2, 1), (4, 3, 11), (4, 5, 6)],
        [(5, 3, 1)]
    ]
    start = 1
    sol = dijkstra(g, start)
    print(sol[1:])


if __name__ == "__main__":
    main()
