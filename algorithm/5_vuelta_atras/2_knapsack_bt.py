""" OLD
import copy

def is_solution(sol, data):
    return sol['w'] + min(data['w']) > data['W']


def is_feasible(sol, data, i):
    return sol['w']+data['w'][i] <= data['W']


def add(sol, data, i):
    sol['o'][i] += 1
    sol['v'] += data['v'][i]
    sol['w'] += data['w'][i]

def remove(sol, data, i):
    sol['o'][i] -= 1
    sol['v'] -= data['v'][i]
    sol['w'] -= data['w'][i]


def knapsack_bt(data, sol, best_sol, k):
    if is_solution(sol, data):
        print(f"EXPLORADA -> {sol}")
        if sol['v'] > best_sol['v']:
            best_sol = copy.deepcopy(sol)
    else:
        for i in range(k, data['n']):
            if is_feasible(sol, data, i):
                add(sol, data, i)
                best_sol = knapsack_bt(data, sol, best_sol, i)
                remove(sol, data, i)
    return best_sol



data = {'n': 4, 'W': 8, 'w': [2,3,4,5], 'v':[3,5,6,10]}
sol = {'o': [0]*data['n'], 'v': 0, 'w': 0}
best_sol = {'o': [0]*data['n'], 'v': 0, 'w': 0}
best_sol = knapsack_bt(data, sol, best_sol, 0)
print(best_sol)
"""

""" BEST
Greedy (voraz)   → puede partir objetos (fraccionaria)
Backtracking     → no puede partir, es 0 o 1 (entera)

Greedy    → coge el mejor ratio v/w, mete fracción si no cabe → rápido O(n log n)
Backtrack → prueba TODAS las combinaciones → lento O(2^n) pero SIEMPRE óptimo

copy es un módulo de Python para copiar objetos.
copy      → copia el contenedor pero no lo que hay dentro
deepcopy  → copia absolutamente todo

-----------------------------
data  # datos del problema
  n   # number of items → número de objetos
  W   # Weight → capacidad máxima mochila
  w   # weights → peso de cada objeto
  v   # values → valor de cada objeto

sol   # solución actual
  o   # objects → 1 si metido, 0 si no
  v   # value → valor acumulado
  w   # weight → peso acumulado

best  # mejor solución encontrada hasta ahora
k     # índice desde donde seguimos probando objetos
"""
import copy

def knapsack_bt(data, sol, best, k):
    if sol['w'] + min(data['w']) > data['W']:  # no cabe nada más
        if sol['v'] > best['v']:
            best = copy.deepcopy(sol)
    else:
        for i in range(k, data['n']):
            if sol['w'] + data['w'][i] <= data['W']:  # cabe objeto i
                sol['o'][i] += 1
                sol['v'] += data['v'][i]
                sol['w'] += data['w'][i]
                best = knapsack_bt(data, sol, best, i)
                sol['o'][i] -= 1                       # backtrack
                sol['v'] -= data['v'][i]
                sol['w'] -= data['w'][i]
    return best

data = {'n': 4, 'W': 8, 'w': [2,3,4,5], 'v': [3,5,6,10]}
sol  = {'o': [0]*data['n'], 'v': 0, 'w': 0}
best = {'o': [0]*data['n'], 'v': 0, 'w': 0}
best = knapsack_bt(data, sol, best, 0)
print(best)