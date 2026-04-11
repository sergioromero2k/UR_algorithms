def dfs_alcanzable(grafo, v, visited):
    visited.add(v)
    for neighbor in grafo[v]:
        if neighbor not in visited:
            dfs_alcanzable(grafo, neighbor, visited)


def main() -> None:
    n, m = map(int, input().strip().split())
    grafo = [[] for _ in range(n)]
    for _ in range(m):
        c1, c2 = map(int, input().strip().split())
        grafo[c1].append(c2)

    alcanzable = []
    for v in range(n):
        visitados = set()
        dfs_alcanzable(grafo, v, visitados)
        visitados.discard(v)
        alcanzable.append(visitados)

    p = int(input().strip())
    respuestas = []
    for _ in range(p):
        p1, p2 = map(int, input().strip().split())
        if p2 in alcanzable[p1]:
            respuestas.append("ANTES")
        elif p1 in alcanzable[p2]:
            respuestas.append("DESPUES")
        else:
            respuestas.append("A LA VEZ")

    print("\n".join(respuestas), end="")

if __name__ == "__main__":
    main()

