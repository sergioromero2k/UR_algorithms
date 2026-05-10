def max_crossing(v, low, mid, high):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += v[i]
        if total > left_sum:
            left_sum = total

    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, high + 1):
        total += v[i]
        if total > right_sum:
            right_sum = total

    return left_sum + right_sum


def max_subarray(v, low, high):
    if low == high:
        return v[low]
    mid = (low + high) // 2
    left  = max_subarray(v, low, mid)
    right = max_subarray(v, mid + 1, high)
    cross = max_crossing(v, low, mid, high)
    return max(left, right, cross)


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    v = list(map(int, input().split()))
    print(max_subarray(v, 0, n - 1))