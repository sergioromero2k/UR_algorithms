#!/usr/bin/env python3
import random, time

def max_vector_trad(v):
    """Metodo tradicional"""
    maximo = v[0]
    for i in range(1, len(v)):
        maximo = max(maximo, v[i])
    return maximo

def max_vector_dyv(v):
    """Poca eficiencia..."""
    if len(v) == 1:
        return v[0]
    else:
        mitad = len(v) //2
        izq = max_vector_dyv(v[:mitad])
        der = max_vector_dyv(v[mitad:])
        return max(izq, der)

def max_vector_dyv_efficient(v, l, h):
    """Buena eficiencia..."""
    if l == h:
        return v[l]
    else:
        mitad = (l+h) //2
        izq = max_vector_dyv_efficient(v, l, mitad)
        der = max_vector_dyv_efficient(v, mitad + 1 , h)
    return max(izq, der)


def main() -> None:
    nVals = [10,100, 1000, 10000, 100000, 100000]
    for n in nVals:
        print(n)
        v = random.sample(range(n*10), n)
        print("Método clásico:", end=" ")
        init = time.time()
        mt = max_vector_trad(v)
        print(time.time() - init, end= "")
        print("Método dyv: ", end= " ")
        init = time.time()
        mdyv = max_vector_dyv(v)
        print(time.time() - init, end=" ")
        print("Método dyv efficient: ", end= " ")
        init = time.time()
        mdyv = max_vector_dyv_efficient(v, 0, len(nVals)-1)
        print(time.time() - init, end=" ")




if __name__ == "__main__":
    main()

