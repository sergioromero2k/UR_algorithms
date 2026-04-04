import heapq


def lexical_topsort(grafo):
    # 1. Calcular grados de entrada
    in_degree = {u: 0 for u in grafo}
    for u in grafo:
        for v in grafo[u]:
            in_degree[v] += 1

    # 2. Cola de prioridad con los que no tienen dependencias
    # heapq siempre saca el menor elemento (orden lexicográfico)
    pq = [u for u in grafo if in_degree[u] == 0]
    heapq.heapify(pq)

    resultado = []

    while pq:
        u = heapq.heappop(pq)
        resultado.append(u)

        for vecino in grafo[u]:
            in_degree[vecino] -= 1
            if in_degree[vecino] == 0:
                heapq.heappush(pq, vecino)

    if len(resultado) != len(grafo):
        print("¡Error! El grafo tiene un ciclo y no se puede ordenar.")
        return []

    # Si el resultado no tiene todos los nodos, hay un ciclo
    return resultado