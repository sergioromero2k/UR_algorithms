#!/usr/bin/env python3

def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid+1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:



def solve_chaos(arr, temp_arr, left, right):
    if left < right:
        mid = (left +right) // 2
        inv_count += solve_chaos(arr, temp_arr, left, mid)
        inv_count += solve_chaos(arr, temp_arr, mid+1, right)
        inv_count += merge(arr, temp_arr, left, mid,  right)
    return inv_count




def main() -> None:
    n = int(input().strip())
    for _ in range(n):
        arr = list(map(int, input().strip().split()))
        temp_arr = arr.copy()
        sol = solve_chaos(arr, temp_arr, 0, len(arr) - 1)
