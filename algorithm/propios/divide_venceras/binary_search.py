#!/usr/bin/env python3

def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

def main() -> None:
    arr = [2, 5, 8, 12, 16, 23, 38, 45]
    resultado = binary_search(arr, 23, 0, len(arr)-1)
    print(resultado)

if __name__ == "__main__":
    main()
