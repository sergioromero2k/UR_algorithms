#!/usr/bin/env python3

def dfs(grafo, v, visited, recorrido):
    visited.add(v)
    recorrido.append(v)
    for nodo in grafo[v]:
        if nodo not in visited:
            dfs(grafo, nodo, visited, recorrido)
    return recorrido


def dfs_completo(grafo, origen):
    """
    Realiza un DFS completo sobre el grafo desde el nodo origen.

    A diferencia del DFS simple, este método garantiza que todos los
    nodos sean visitados aunque el grafo sea no conexo. El DFS anterior
    solo exploraba la componente conectada al nodo origen, dejando sin
    visitar los nodos aislados o en componentes desconectadas.

    :param grafo: lista de adyacencia donde grafo[v] contiene los vecinos de v
    :param origen: nodo desde el que se inicia el recorrido
    :return recorrido: lista con el orden de visita de todos los nodos
    """
    visited = set()
    recorrido = []

    dfs(grafo, origen, visited, recorrido)
    for v in range(1, len(grafo)):
        if v not in visited:
            dfs(grafo, v, visited, recorrido)
    return recorrido


def main() ->None:
    grafo = [
        [],
        [2, 4, 8],
        [1, 3, 4],
        [2, 4, 5],
        [1, 2, 3, 7],
        [3, 6],
        [5, 7],
        [4, 6, 9],
        [1, 9],
        [7, 8]
    ]

    print(dfs_completo(grafo, 1))  # desde nodo 1
    print(dfs_completo(grafo, 5))  # desde nodo 5
    print(dfs_completo(grafo, 9))  # desde nodo 9

if __name__ == "__main__":
    main()
