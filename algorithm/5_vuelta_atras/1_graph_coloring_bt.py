"""OLD
def is_solution(v, g):
    return v == len(g)

def is_feasible(g, sol, v, color):
    feasible = True
    i = 0
    while feasible and i < len(g[v]):
        adj = g[v][i]
        if adj < v:
            feasible = color != sol[adj]
        i += 1
    return feasible

def graph_coloring_bt(g, m, sol, v):
    if is_solution(v, g):
        is_sol = True
    else:
        is_sol = False
        color = 1
        while not is_sol and color <= m:
            if is_feasible(g, sol, v, color):
                sol[v] = color
                sol, is_sol = graph_coloring_bt(g, m, sol, v+1)
                if not is_sol:
                    sol[v] = -1
            color += 1
    return sol, is_sol

g = [
    [1, 2, 3],
    [0],
    [0, 3],
    [0, 2]
]
m = 3
start = 0
sol = [-1] * len(g)
sol, is_sol = graph_coloring_bt(g, m, sol, start)
if is_sol:
    print(sol)
else:
    print("La instancia del problema no tiene solucion")
"""



"""BEST
Colorea un grafo con m colores de forma que dos nodos adyacentes nunca tengan el mismo color.

g    # graph → lista de adyacencia del grafo
m    # máximo número de colores disponibles
sol  # solution → color asignado a cada nodo, -1 = sin asignar
v    # vertex → nodo actual que estamos coloreando

all(color != sol[adj] for adj in g[v] if adj < v)
#   ↑                       ↑              ↑
# ningún vecino          vecinos de v   solo los ya coloreados
# tiene mi color                        (adj < v)
"""
def graph_coloring_bt(g, m, sol, v):
    if v == len(g):
        return sol, True
    
    for color in range(1, m+1):
        if all(color != sol[adj] for adj in g[v] if adj < v):  # is_feasible
            sol[v] = color
            sol, ok = graph_coloring_bt(g, m, sol, v+1)
            if ok:
                return sol, True
            sol[v] = -1  # backtrack
    
    return sol, False

g = [[1,2,3], [0], [0,3], [0,2]]
m = 3
sol = [-1] * len(g)
sol, ok = graph_coloring_bt(g, m, sol, 0)
print(sol if ok else "Sin solución")