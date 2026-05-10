from collections import deque

def bfs(grid, N, M, start, end, recompensas_validas, recompensas_trampa):
    n_rec = len(recompensas_validas)
    rec_index = {r: i for i, r in enumerate(recompensas_validas)}
    meta = (1 << n_rec) - 1

    dist = {}
    estado_inicial = (start[0], start[1], 0)
    dist[estado_inicial] = 0
    queue = deque([estado_inicial])

    while queue:
        r, c, mask = queue.popleft()
        d = dist[(r, c, mask)]

        if (r, c) == end and mask == meta:
            return d

        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if grid[nr][nc] == 'w' or grid[nr][nc] == 't':
                continue
            if (nr, nc) in recompensas_trampa:
                continue

            new_mask = mask
            if (nr, nc) in rec_index:
                new_mask |= (1 << rec_index[(nr, nc)])

            nuevo_estado = (nr, nc, new_mask)
            if nuevo_estado not in dist:
                dist[nuevo_estado] = d + 1
                queue.append(nuevo_estado)

    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input().split())

    torretas = set()
    recompensas = []
    start = end = None

    for i in range(N):
        for j in range(M):
            c = grid[i][j]
            if c == 't':   torretas.add((i, j))
            elif c == 's': start = (i, j)
            elif c == 'e': end = (i, j)
            elif c == 'r': recompensas.append((i, j))

    celdas_peligrosas = set()
    for ti, tj in torretas:
        celdas_peligrosas.add((ti, tj))
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < M:
                celdas_peligrosas.add((ni, nj))

    recompensas_trampa  = set(r for r in recompensas if r in celdas_peligrosas)
    recompensas_validas = [r for r in recompensas if r not in celdas_peligrosas]

    print(bfs(grid, N, M, start, end, recompensas_validas, recompensas_trampa))