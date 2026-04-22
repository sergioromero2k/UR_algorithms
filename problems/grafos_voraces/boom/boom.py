#!/usr/bin/env python3

def obtener_nodo_mas_cercano(distancias, visitado):
    nodo_siguiente = -1
    distancia_minima = 0x3f3f3f3f
    for nodo in range(len(distancias)):
        if not visitado[nodo] and distancias[nodo] < distancia_minima:
            nodo_siguiente = nodo
            distancia_minima = distancias[nodo]
    return nodo_siguiente

def dijkstra(grafo, nodo_inicio, num_nodos):
    distancias = [0x3f3f3f3f] * num_nodos
    visitado = [False] * num_nodos
    distancias[nodo_inicio] = 0

    for _ in range(num_nodos):
        actual = obtener_nodo_mas_cercano(distancias, visitado)
        if actual == -1:
            break
        visitado[actual] = True
        for destino, peso in grafo[actual]:
            nueva_distancia = distancias[actual] + peso
            if nueva_distancia < distancias[destino]:
                distancias[destino] = nueva_distancia

    return distancias

def main():
    N, M = map(int, input().split())
    tipos = list(map(int, input().split()))

    grafo = [[] for _ in range(N)]
    for _ in range(M):
        c, d, l = map(int, input().split())
        grafo[c].append((d, l))
        grafo[d].append((c, l))

    # Agrupar nodos por tipo
    nodos_por_tipo = {}
    for i in range(N):
        t = tipos[i]
        if t not in nodos_por_tipo:
            nodos_por_tipo[t] = []
        nodos_por_tipo[t].append(i)

    resultados = []
    for tipo in sorted(nodos_por_tipo.keys()):
        nodos = nodos_por_tipo[tipo]
        min_distancia = 0x3f3f3f3f

        for u in nodos:
            dist = dijkstra(grafo, u, N)
            for v in nodos:
                if v != u and dist[v] < min_distancia:
                    min_distancia = dist[v]

        resultados.append(min_distancia)

    print(*resultados)

if __name__ == "__main__":
    main()