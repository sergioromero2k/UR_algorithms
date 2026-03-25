
def busc_bin_it(v ,x):
    l = 0
    h = len(v) - 1
    while l  <= h:
        mid = (l+h) //2
        if v[mid] == x:
            return mid
        elif v[mid] == x:
            l = mid +1
        else:
            h =mid-1
    return -l


def main() -> None:
    v = [1, 3, 5, 7, 8, 10, 12, 15]
    l = 0
    h = len(v) -1
    x = 3
    posicion = busc_bin_it(v, x, l, h)
    if posicion >= 0:
        print("El elemento", x, "está en la posición", posicion)
    else:
        print("El elemento", x, "no está en el vector, deberia estar en la posición", posicion)