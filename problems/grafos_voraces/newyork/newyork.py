#!/usr/bin/env python3

def select_min(distancia, visited):
    min_node = -1
    min_dist = float('inf')

    for nodo in range(len(distancia)):
        if not visited[nodo] and distancia[nodo] < min_dist:
            min_dist = distancia[nodo]
            min_node = nodo
    return min_node

def dijkstra(grafo, inicio):
    n = len(grafo)
    distance = [float('inf')] * n
    visited = [False] * n

    distance[inicio] = 0

    for _ in range(n):
        u = select_min(distance, visited)
        if u == -1:
            break

        visited[u] = True
        for src, dst, w in grafo[u]:
            if distance[src] + w < distance[dst]:
                distance[dst] = distance[src] + w

    return distance

def main() -> None:
    n, m = map(int, input().strip().split())
    grafo = [[] for _ in range(n)]
    for _ in range(m):
        a, b, t = map(int, input().strip().split())
        grafo[a].append((a,b,t))
        grafo[b].append((b,a,t))

    sumas = []
    for i in range(n):
        dist =dijkstra(grafo, i)
        total = sum(d for d in dist if d != float('inf'))
        sumas.append(total)

    print(min(sumas))
    for i, s in enumerate(sumas):
        print(f"{i}: {s}")

if __name__ == "__main__":
    main()
