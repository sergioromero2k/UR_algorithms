from collections import deque


def bfs(grid, N, M, start, end):
    # Estado: (fila, col)
    # Queremos maximizar recompensas y minimizar saltos
    # dist[estado] = (recompensas, saltos)

    movimientos = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    inicio_rec = 1 if grid[start[0]][start[1]] == 1 else 0

    # dist[r][c] = (max_recompensas, min_saltos)
    dist = [[None] * M for _ in range(N)]
    dist[start[0]][start[1]] = (inicio_rec, 0)
    queue = deque([(start[0], start[1], inicio_rec, 0)])

    while queue:
        r, c, rec, saltos = queue.popleft()

        for dr, dc in movimientos:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if grid[nr][nc] == -1:
                continue

            nueva_rec = rec + (1 if grid[nr][nc] == 1 else 0)
            nuevos_saltos = saltos + 1

            actual = dist[nr][nc]
            # Actualizar si: mas recompensas, o igual recompensas y menos saltos
            if actual is None or nueva_rec > actual[0] or \
                    (nueva_rec == actual[0] and nuevos_saltos < actual[1]):
                dist[nr][nc] = (nueva_rec, nuevos_saltos)
                queue.append((nr, nc, nueva_rec, nuevos_saltos))

    resultado = dist[end[0]][end[1]]
    if resultado is None:
        print("Consigo 0 recompensas en 0 saltos")
    else:
        print(f"Consigo {resultado[0]} recompensas en {resultado[1]} saltos")


if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    start = (0, 0)
    end = (N - 1, M - 1)

    bfs(grid, N, M, start, end)