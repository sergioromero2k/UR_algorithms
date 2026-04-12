def calcular_prefix_sum(arr):
    n = len(arr)
    prefix = [0]*n

    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix


def suma_subarreglo(prefix, izq, der):
    if izq == 0:
        return prefix[der]
    else:
        return prefix[der] - prefix[izq -1]

def main() -> None:
    arr = [2, 4, 6, 8, 10]
    prefix = calcular_prefix_sum(arr)

    print("Array original:", arr)
    print("Prefix sum:", prefix)

    resultado = suma_subarreglo(prefix, 1, 3)
    print(f"Suma de índices 1 a 3: {resultado}")

if __name__ == "__main__":
    main()