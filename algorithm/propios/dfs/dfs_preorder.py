def dfs(grafo, v, recorrido, visited):
    # Grafo conexo
    visited[v] = True
    recorrido.append(v)
    for nodo in grafo[v]:
        if not visited[nodo]:
            dfs(grafo, nodo, recorrido, visited)
    return recorrido


def main() -> None:
    # Grafo no dirigido
    grafo = [
        [],  # índice 0 no se usa
        [2, 4, 8],  # nodo 1 conectado a 2, 4, 8
        [1, 3, 4],  # nodo 2 conectado a 1, 3, 4
        [2, 4, 5],  # nodo 3 conectado a 2, 4, 5
        [1, 2, 3, 7],  # nodo 4 conectado a 1, 2, 3, 7
        [3, 6],  # nodo 5 conectado a 3, 6
        [5, 7],  # nodo 6 conectado a 5, 7
        [4, 6, 9],  # nodo 7 conectado a 4, 6, 9
        [1, 9],  # nodo 8 conectado a 1, 9
        [7, 8]  # nodo 9 conectado a 7, 8
    ]
    recorrido = []
    visited = [False] * (len(grafo))
    print(dfs(grafo, 1, recorrido, visited))


if __name__ == "__main__":
    main()
