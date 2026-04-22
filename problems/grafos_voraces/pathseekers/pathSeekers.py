#!/usr/bin/env python3

def dijkstra(g, n, target):
    distances = [0x3f3f3f3f] * n
    visited = [False] * n
    prev = [-1] * n
    distances[0] = 0
    visited[0] = True

    # Primera pasada: aristas que salen del nodo 0
    for dst, w, p in g[0]:
        if p == -1 or (p < n and visited[p]):
            if w < distances[dst]:
                distances[dst] = w
                prev[dst] = 0

    # Ciclo principal de las fotos
    for _ in range(2, n + 1):
        next_node = -1
        min_dist = 0x3f3f3f3f
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                next_node = i
                min_dist = distances[i]

        if next_node == -1 or min_dist == 0x3f3f3f3f:
            break

        visited[next_node] = True
        for dst, w, p in g[next_node]:
            if p == -1 or (p < n and visited[p]):
                new_dist = distances[next_node] + w
                if new_dist < distances[dst]:
                    distances[dst] = new_dist
                    prev[dst] = next_node

    if distances[target] == 0x3f3f3f3f:
        return None, None

    path = []
    node = target
    while node != -1:
        path.append(node)
        node = prev[node]
    path.reverse()

    return path, distances[target]


def main():
    try:
        linea_ini = input().split()
        if not linea_ini: return
        n, m = map(int, linea_ini)

        g = [[] for _ in range(n)]
        for _ in range(m):
            o, d, w, p = map(int, input().split())
            g[o].append((d, w, p))

        k_linea = input().strip()
        if not k_linea: return
        k = int(k_linea)

        resultados = []
        for _ in range(k):
            target_node = int(input())
            path, cost = dijkstra(g, n, target_node)

            if path is None:
                resultados.append("MISION FALLIDA")
            else:
                res_str = f"{' '.join(map(str, path))} - {cost}"
                resultados.append(res_str)

        for r in resultados:
            print(r)

    except EOFError:
        pass


if __name__ == "__main__":
    main()