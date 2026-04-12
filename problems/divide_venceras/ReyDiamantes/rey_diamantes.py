#!/usr/bin/env python3

def bisect_left(arr, p):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] >= p:
            high = mid
        else:
            low = mid + 1
    return low

def main() -> None:
    n = int(input())

    grid = []
    for _ in range(n):
        fila = list(map(int, input().strip().split()))
        grid.append(fila)

    plano = [valor for fila in grid for valor in fila ]

    ataque = list(map(int, input().strip().split()))

    for a in ataque:
        pos = bisect_left(plano, a)
        eliminado = plano[pos]
        plano[pos] = float('inf')
        for i in range(n):
            for j in range(n):
                if grid[i][j] == eliminado:
                    grid[i][j] = "X"

    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
