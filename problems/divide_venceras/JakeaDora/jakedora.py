#!/usr/bin/env python3

def bisect_left(arr, p1):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) //2
        if arr[mid] >= p1:
            high = mid
        else:
            low = mid + 1
    return low

def bisect_right(arr, p2):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > p2:
            high = mid
        else:
            low = mid + 1
    return low



def main() -> None:
    n, a = map(int, input().strip().split())
    numbers = list(map(int, input().strip().split()))
    if len(numbers) != n:
        return

    numbers = sorted(numbers)
    attacks = []
    for _ in range(a):
        id, p1, p2 = map(int, input().strip().split())
        attacks.append((id, p1, p2))

    resultados = []
    for id, p1, p2 in attacks:
        cantidad = bisect_right(numbers, p2) - bisect_left(numbers, p1)
        resultados.append((id, cantidad))

    max_count = max(cantidad for id, cantidad in resultados)
    ids =  [id for id, cantidad in resultados if cantidad == max_count]

    print(*ids)
    print(max_count)

if __name__ == "__main__":
    main()

