

def busc_bin_rec(v, x, l, h):
    if l > h:
        return -l
    else:
        mitad = (l+h) // 2
        if v[mitad] == x:
            return mitad
        elif v[mitad] < x:
            return busc_bin_rec(v, x, mitad + 1, h)
        else:
            return busc_bin_rec(v, x, l, mitad -1)


def main() -> None:
    v = [1, 3, 5, 7, 8, 10, 12, 15]
    l = 0
    h = len(v) -1
    x = 3
    posicion = busc_bin_rec(v, x, l, h)
    if posicion >= 0:
        print("El elemento", x, "está en la posición", posicion)
    else:
        print("El elemento", x, "no está en el vector, deberia estar en la posición", posicion)