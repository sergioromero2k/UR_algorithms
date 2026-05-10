from collections import deque

def bfs(grid, N, M):
    # Estado: (fila, col, turno)
    # Turno empieza en 1 al estar en (0,0)
    if grid[0][0] == -1:
        return None

    dist = {}
    estado_inicial = (0, 0, 1)
    dist[estado_inicial] = 0
    queue = deque([estado_inicial])

    while queue:
        r, c, turno = queue.popleft()
        pasos = dist[(r, c, turno)]

        if r == N-1 and c == M-1:
            return pasos

        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if grid[nr][nc] == -1:
                continue

            nuevo_turno = turno + 1
            # La celda solo es transitable si turno <= valor celda
            if nuevo_turno > grid[nr][nc]:
                continue

            nuevo = (nr, nc, nuevo_turno)
            if nuevo not in dist:
                dist[nuevo] = pasos + 1
                queue.append(nuevo)

    return None


if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    resultado = bfs(grid, N, M)
    if resultado is None:
        print("NO HAY SALIDA")
    else:
        print(resultado)