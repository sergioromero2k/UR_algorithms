import sys
from collections import deque


def bfs(grid, n, m, start, vecna, mentos, coca):
    # El estado inicial comprueba si la posición de inicio ya tiene los objetos [cite: 18, 19]
    init_m = (start == mentos)
    init_c = (start == coca)

    # Estado: (fila, columna, tiene_mentos, tiene_coca)
    estado_inicial = (start[0], start[1], init_m, init_c)

    # Cola para BFS: (estado, distancia)
    queue = deque([(estado_inicial, 0)])
    # Conjunto de visitados para evitar ciclos y optimizar tiempo [cite: 21, 22]
    visited = {estado_inicial}

    while queue:
        (r, c, tm, tc), dist = queue.popleft()

        # Condición de victoria: estar en la posición de Vecna con ambos objetos
        if (r, c) == vecna and tm and tc:
            return dist

        # Explorar los 4 movimientos posibles (habitación por habitación) [cite: 10, 18]
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            # Verificar límites de la fortaleza y que no sea una pared 'W' [cite: 9, 11]
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 'W':
                # Actualizar si se recogen los caramelos o la Coca Cola [cite: 5, 15, 16]
                ntm = tm or (nr, nc) == mentos
                ntc = tc or (nr, nc) == coca

                nuevo_estado = (nr, nc, ntm, ntc)
                if nuevo_estado not in visited:
                    visited.add(nuevo_estado)
                    queue.append((nuevo_estado, dist + 1))

    return -1


def main():
    # Lectura de las dimensiones N y M [cite: 9]
    linea = sys.stdin.readline().split()
    if not linea:
        return
    n, m = map(int, linea)

    grid = []
    start = vecna = mentos = coca = None

    # Procesamiento de la fortaleza habitación por habitación [cite: 10]
    for i in range(n):
        # Leemos la fila eliminando espacios en blanco
        fila_raw = "".join(sys.stdin.readline().split())
        fila = list(fila_raw)
        grid.append(fila)

        # Identificar las posiciones clave en el mapa [cite: 13, 14, 15, 16]
        for j in range(len(fila)):
            char = fila[j]
            if char == 'P':
                start = (i, j)
            elif char == 'V':
                vecna = (i, j)
            elif char == 'M':
                mentos = (i, j)
            elif char == 'C':
                coca = (i, j)

    # Cálculo de la ruta más corta
    resultado = bfs(grid, n, m, start, vecna, mentos, coca)

    if resultado == -1:
        print("Imposible")
    else:
        # El resultado no cuenta la posición inicial como paso
        print(resultado)


if __name__ == "__main__":
    main()