#!/usr/bin/env python3

from collections import deque

def bfs(laberinto, n, m):
    cola = deque()
    visited = set()

    cola.append((0, 0, 1))
    visited.add((0, 0, 1%2))

    while cola:
        f, c, turno = cola.popleft()
        if laberinto[f][c] == 2:
            return turno - 1

        for df, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nf, nc = f+df, c+dc
            nuevo_turno = turno + 1
            estado = (nf, nc, nuevo_turno%2)
            if 0 <= nf < n and 0 <= nc < m and estado not in visited:
                celda = laberinto[nf][nc]
                if celda == -1 and turno % 2 == 0:
                    continue
                visited.add(estado)
                cola.append((nf, nc, nuevo_turno))

    return -1


def main():
    n, m = map(int, input().split())
    laberinto = []
    for _ in range(n):
        fila = list(map(int, input().split()))
        laberinto.append(fila)

    print(bfs(laberinto, n, m))

if __name__ == "__main__":
    main()