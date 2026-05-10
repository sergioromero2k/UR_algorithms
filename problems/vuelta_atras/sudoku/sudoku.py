def is_feasible(grid, row, col, num):
    # Verificar fila
    if num in grid[row]:
        return False
    # Verificar columna
    for i in range(9):
        if grid[i][col] == num:
            return False
    # Verificar subcuadro 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

def sudoku_bt(grid, celdas, idx):
    if idx == len(celdas):
        return True
    row, col = celdas[idx]
    for num in range(1, 10):
        if is_feasible(grid, row, col, num):
            grid[row][col] = num
            if sudoku_bt(grid, celdas, idx + 1):
                return True
            grid[row][col] = 0
    return False


if __name__ == "__main__":
    grid = []
    for _ in range(9):
        grid.append(list(map(int, input().split())))

    celdas_vacias = [
        (i, j) for i in range(9) for j in range(9) if grid[i][j] == 0
    ]

    sudoku_bt(grid, celdas_vacias, 0)

    for row in grid:
        print(*row)