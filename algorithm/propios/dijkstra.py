import heapq

def dijkstra(grafo, inicio):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[inicio] = 0

    cola = [(0, inicio)]

    while cola:
        d_actual, nodo = heapq.heappop(cola)

        if d_actual > dist[nodo]:
            continue

        for vecino, peso in grafo[nodo]:
            nueva_dist = dist[nodo] + peso
            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist
                heapq.heappush(cola, (nueva_dist, vecino))

    return dist

def main() -> None:
    grafo = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 2)],
    'C': [('D', 5)],
    'D': []
    }
    print(dijkstra(grafo, 'A'))


if __name__ == "__main__":
    main()
