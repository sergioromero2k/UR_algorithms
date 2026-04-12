#!/usr/bin/env python3

def binary_search(prefix, v, k):
    low = 0
    high = len(prefix) - 1 - k

    while low < high:
        mid = (low+high) // 2
        suma = prefix[mid + k] - prefix[mid]

        if suma > v:
            high = mid
        else:
            low = mid + 1
    return low, prefix[low+k] - prefix[low]

def calcular_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n+1)
    prefix[0] = 0

    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + arr[i-1]

    return prefix


def main() -> None:
    n = int(input())
    number = list(map(int, input().strip().split()))
    if len(number) != n:
        return

    number_prefix = calcular_prefix_sum(number)
    m = int(input())

    show = []
    for _ in range(m):
        v, k = map(int, input().strip().split())
        pos, suma = binary_search(number_prefix, v, k)
        show.append((pos, suma))

    for pos, suma in show:
        print(pos, suma)


if __name__ == "__main__":
    main()
