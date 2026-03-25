def buscar_nodo_mas_cercano(costes, visitados):
    nodo_minimo = 0
    distancia_minima = float('inf')

    for i in range(1, len(costes)):
        if not visitados[i] and costes[i] < distancia_minima:
            nodo_minimo = i
            distancia_minima = costes[i]
    return nodo_minimo


def dijkstra_entendible(grafo, nodo_inicio):
    num_nodos = len(grafo) - 1

    costes_acumulados = [float('inf')] * (num_nodos + 1)
    visitados = [False] * (num_nodos + 1)

    costes_acumulados[nodo_inicio] = 0

    for _ in range(num_nodos):
        actual = buscar_nodo_mas_cercano(costes_acumulados, visitados)

        if actual == 0:
            break

        visitados[actual] = True

        for _, destino, peso in grafo[actual]:
            nuevo_coste = costes_acumulados[actual] + peso

            if nuevo_coste < costes_acumulados[destino]:
                costes_acumulados[destino] = nuevo_coste

    return costes_acumulados

def main() -> None:

    grafo_ciudades = [
        [],  # Nodo 0 (vacio)
        [(1, 2, 5), (1, 4, 3)],  # Conexiones desde el nodo 1
        [(2, 5, 1)],  # Desde el 2
        [],  # Desde el 3
        [(4, 2, 1), (4, 3, 11), (4, 5, 6)],  # Desde el 4
        [(5, 3, 1)]  # Desde el 5
    ]

    resultado = dijkstra_entendible(grafo_ciudades, 1)
    print(f"Costes mínimos desde el nodo 1: {resultado[1:]}")


if __name__ == "__main__":
    main()


"""
def obtener_nodo_mas_cercano(distancias, visitado):
    nodo_siguiente = 0
    distancia_minima = float('inf')
    
    for nodo in range(1, len(distancias)):
        if not visitado[nodo] and distancias[nodo] < distancia_minima:
            nodo_siguiente = nodo
            distancia_minima = distancias[nodo]
    
    return nodo_siguiente


def dijkstra(grafo, nodo_inicio):
    num_nodos = len(grafo) - 1
    
    distancias = [float('inf')] * (num_nodos + 1)
    visitado = [False] * (num_nodos + 1)
    
    distancias[nodo_inicio] = 0
    visitado[nodo_inicio] = True
    
    # Inicializar distancias desde el nodo inicial
    for origen, destino, peso in grafo[nodo_inicio]:
        distancias[destino] = peso
    
    # Iterar sobre el resto de nodos
    for _ in range(2, num_nodos + 1):
        nodo_actual = obtener_nodo_mas_cercano(distancias, visitado)
        visitado[nodo_actual] = True
        
        for origen, destino, peso in grafo[nodo_actual]:
            nueva_distancia = distancias[origen] + peso
            if nueva_distancia < distancias[destino]:
                distancias[destino] = nueva_distancia
    
    return distancias


grafo = [
    [],
    [(1,2,5),(1,4,3)],
    [(2,5,1)],
    [],
    [(4,2,1),(4,3,11),(4,5,6)],
    [(5,3,1)]
]

nodo_inicio = 1
resultado = dijkstra(grafo, nodo_inicio)
print(resultado[1:])
"""