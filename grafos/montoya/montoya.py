from collections import deque

def bfs_aux(grafo, origen, destino, visitado):
    visitado[origen] = True
    cola = deque()
    cola.append((origen, 0))

    while cola:
        nodo_actual, dist = cola.popleft()
        if nodo_actual == destino:
            return dist + 1
        for vecino in grafo[nodo_actual]:
            if not visitado[vecino]:
                cola.append((vecino, dist + 1))
                visitado[vecino] = True
    return float('inf')

def bfs(grafo, origen, destino):
    n = len(grafo)
    visitado = [False] * n
    return bfs_aux(grafo, origen, destino, visitado)

def main() -> None:
    n, m, c = map(int, input().strip().split())

    list_ady = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().strip().split())
        list_ady[u].append(v)
        list_ady[v].append(u)

    resultado = []
    comparar = []
    for _ in range(c):
        o, d, p = map(int, input().strip().split())
        resultado.append(bfs(list_ady, o, d))
        comparar.append(p)

    for i in range(len(resultado)):
        if resultado[i] <= comparar[i]:
            print(resultado[i])
        else:
            print("MON TOYA POR FAVOR")

if __name__ == "__main__":
    main()