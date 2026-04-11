#!/usr/bin/env/python3

def merge(v, left, right, count):
    l = 0
    r = 0
    i = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            v[i] = left[l]
            count += 1
            l += 1
        else:
            v[i] = right[r]
            count += len(left) - l
            r += 1
        i += 1

    if r == len(right):
        f = l
        resto = left
    else:
        f = r
        resto = right

    for j in range(f, len(resto)):
        v[i] = resto[j]
        i += 1

    return count

def merge_sort(v):
    if len(v) == 1:
        return 0
    else:
        mid = len(v) // 2
        left = v[:mid]
        right = v[mid:]

        count = 0
        count += merge_sort(left)
        count += merge_sort(right)
        count = merge(v, left, right, count)

        return count

def main() -> None:
    n = int(input())
    num_serie = []
    for i in range(n):
        num_serie.append(list(map(int, input().strip().split())))

    count = merge_sort(num_serie[0])
    print(num_serie[0])
    print(count)


if __name__ == "__main__":
    main()
