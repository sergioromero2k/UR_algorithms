def mover(grid, N, r, c, dr, dc):
    """Devuelve (celda_final, pasos) — el erizo para solo al chocar."""
    nr, nc = r + dr, c + dc
    pasos = 0
    ultima_r, ultima_c = r, c
    while 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 3:
        ultima_r, ultima_c = nr, nc
        pasos += 1
        nr += dr
        nc += dc
    if pasos == 0:
        return None, 0
    return (ultima_r, ultima_c), pasos


def dijkstra(grid, N, start, end, anillos):
    n_anillos = len(anillos)
    anillo_idx = {a: i for i, a in enumerate(anillos)}
    meta = (1 << n_anillos) - 1

    mask_inicio = 0
    if start in anillo_idx:
        mask_inicio |= (1 << anillo_idx[start])

    estado_inicial = (start[0], start[1], mask_inicio)
    dist = {estado_inicial: 0}
    heap = [(0, start[0], start[1], mask_inicio)]

    while heap:
        d, r, c, mask = heap[0]
        heapq.heappop(heap)

        if (r, c) == end and mask == meta:
            return d

        if dist.get((r, c, mask), float('inf')) < d:
            continue

        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            celda, pasos = mover(grid, N, r, c, dr, dc)
            if celda is None:
                continue

            nr, nc = celda
            new_mask = mask
            # Recoger anillos en el camino
            tr, tc = r + dr, c + dc
            while (tr, tc) != (nr + dr, nc + dc):
                if (tr, tc) in anillo_idx:
                    new_mask |= (1 << anillo_idx[(tr, tc)])
                tr += dr
                tc += dc

            nuevo_dist = d + pasos
            nuevo = (nr, nc, new_mask)
            if nuevo_dist < dist.get(nuevo, float('inf')):
                dist[nuevo] = nuevo_dist
                heapq.heappush(heap, (nuevo_dist, nr, nc, new_mask))

    return -1


if __name__ == "__main__":
    import heapq
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    sx, sy, ex, ey = map(int, input().split())
    start = (sx, sy)
    end   = (ex, ey)

    anillos = [
        (i, j) for i in range(N) for j in range(N)
        if grid[i][j] == 1
    ]

    print(dijkstra(grid, N, start, end, anillos))