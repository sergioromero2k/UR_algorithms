#!/usr/bin/env python3


def dfs_aux(nodo_actual, destino, grafo, trampas, visitado, camino):
    if nodo_actual in trampas or nodo_actual in visitado:
        return None

    camino.append(nodo_actual)
    visitado.add(nodo_actual)

    if nodo_actual == destino:
        return camino.copy()

    for vecino in sorted(grafo[nodo_actual]):
        resultado = dfs_aux(vecino, destino, grafo, trampas, visitado, camino)
        if resultado:
            return resultado

    # Backtracking
    camino.pop()
    visitado.remove(nodo_actual)
    return None

def dfs(inicio, destino, trampas, grafo):
    visitado = set()
    camino = []
    resultado = dfs_aux(inicio, destino, grafo, trampas, visitado, camino)

    if resultado:
        print(" ".join(map(str, resultado)))
    else:
        print("Dungeons y Vagos quedan atrapados")


def main() -> None:
    n, m = map(int, input().strip().split())
    grafo = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().strip().split())
        grafo[x].append(y)
        grafo[y].append(x)
    s, t = map(int, input().strip().split())
    trampas = set(map(int, input().strip().split()))

    dfs(s, t, trampas, grafo)

if __name__ == "__main__":
    main()