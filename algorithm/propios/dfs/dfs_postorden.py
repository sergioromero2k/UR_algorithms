def dfs(grafo, v, visited, recorrido):
    # Grafo conexo
    visited[v] = True
    for nodo in grafo[v]:
        if not visited[nodo]:
            dfs(grafo, nodo, visited, recorrido)
    recorrido.append(v)
    return recorrido

def main():
    # Grafo no dirigido
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
    visited = [False] * len(grafo)
    recorrido = []
    print(dfs(grafo, 1, visited, recorrido))


if __name__ == "__main__":
    main()