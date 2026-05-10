def is_sol(g, node):
    return node == g['n']

def is_feasible(g, sol, node, color):
    for adj in g['g'][node]:
        if adj < node and sol[adj] == color:
            return False
    return True

def coloring_va(g, m, sol, node, fijos):
    if is_sol(g, node):
        return sol, True
    found = False
    # Si el nodo tiene color fijo, solo probamos ese
    if node in fijos:
        colores = [1]
    else:
        colores = range(1, m + 1)
    for color in colores:
        if is_feasible(g, sol, node, color):
            sol[node] = color
            sol, found = coloring_va(g, m, sol, node + 1, fijos)
            if found:
                return sol, found
            sol[node] = 0
    return sol, False


if __name__ == "__main__":
    n, m_aristas, s = map(int, input().split())
    g = {'n': n, 'g': [[] for _ in range(n)]}
    for _ in range(m_aristas):
        u, v = map(int, input().split())
        g['g'][u].append(v)
        g['g'][v].append(u)
    fijos = set(map(int, input().split()))

    sol = [0] * n
    # Buscar el minimo numero de canciones que funciona
    for num_canciones in range(1, s + 1):
        sol = [0] * n
        sol, found = coloring_va(g, num_canciones, sol, 0, fijos)
        if found:
            print(num_canciones)
            break
    else:
        print("TODOS FUERA")