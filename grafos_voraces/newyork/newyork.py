
#!/usr/bin/env python3

def mas_cercano(distancia, visitado):
    nodo_sig = 0
    distancia_min =  0x3f3f3f3f

    for nodo in range(len(distancia)):
        if not visitado[nodo] and distancia[nodo] < distancia_min:
            nodo_sig = nodo
            distancia_min =  distancia[nodo]
    return nodo_sig


def dijkstra(grafo, nodo_inicio):
    num_nodos = len(grafo)
    distancias = [float('inf')] * (num_nodos)
    visitados = [False] * (num_nodos)

    distancias[nodo_inicio] = 0
    visitados[nodo_inicio] = 0

    for origen, destino, peso in grafo[nodo_inicio]:
        distancias[destino] = peso

    for _ in range(num_nodos):
        nodo_actual = mas_cercano(distancias, visitados)
        visitados[nodo_actual] = True

        for origen, destino, peso in grafo[nodo_actual]:
            nueva_distancia = distancias[origen] + peso
            if nueva_distancia < distancias[destino]:
                distancias[destino] = nueva_distancia

    print(distancias)

def main() -> None:
    n, m = map(int, input().strip().split())
    grafo = [[] for _ in range(n)]
    for i in range(m):
        a, b, t =  map(int, input().strip().split())
        grafo[i].append((a,b,t))
        grafo[i].append((a,b,t))

    dijkstra(grafo, 0)

if __name__ == "__main__":
    main()