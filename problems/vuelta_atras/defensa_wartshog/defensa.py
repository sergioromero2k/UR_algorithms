import copy

def get_covered(grid, N, M, row, col, R):
    covered = set()
    covered.add((row, col))
    for dc in range(1, R + 1):
        nc = col + dc
        if nc >= M or grid[row][nc] == -1:
            break
        covered.add((row, nc))
    for dc in range(1, R + 1):
        nc = col - dc
        if nc < 0 or grid[row][nc] == -1:
            break
        covered.add((row, nc))
    for dr in range(1, R + 1):
        nr = row + dr
        if nr >= N or grid[nr][col] == -1:
            break
        covered.add((nr, col))
    for dr in range(1, R + 1):
        nr = row - dr
        if nr < 0 or grid[nr][col] == -1:
            break
        covered.add((nr, col))
    return covered


def count_uncovered(grid, N, M, covered):
    return sum(
        1 for i in range(N) for j in range(M)
        if grid[i][j] == 0 and (i, j) not in covered
    )


def wartshog_bt(grid, N, M, R, row, covered, best):
    if row == N:
        uncovered = count_uncovered(grid, N, M, covered)
        if uncovered < best['v']:
            best['v'] = uncovered
        return

    # Poda: si ya tenemos 0 sin cubrir no hace falta seguir
    if best['v'] == 0:
        return

    # Opcion: no colocar en esta fila
    wartshog_bt(grid, N, M, R, row + 1, covered, best)

    # Opcion: colocar en cada columna valida
    for col in range(M):
        if grid[row][col] == 0:
            nuevas = get_covered(grid, N, M, row, col, R)
            # Poda: solo exploramos si esta opcion puede mejorar
            if nuevas - covered:  # si cubre algo nuevo
                wartshog_bt(grid, N, M, R, row + 1, covered | nuevas, best)


if __name__ == "__main__":
    N, M, R = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    total_suelo = sum(
        1 for i in range(N) for j in range(M) if grid[i][j] == 0
    )
    best = {'v': total_suelo}
    wartshog_bt(grid, N, M, R, 0, set(), best)
    print(best['v'])