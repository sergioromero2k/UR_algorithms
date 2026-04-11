#!/usr/bin/env python3

def get_best_item(candidates, v, w):
    best_item = 0
    best_ratio = -1
    for c in candidates:
        ratio = v[c] / w[c]
        if ratio > best_ratio:
            best_item = c
            best_ratio = ratio
    return best_item


def greedy_knapsack(v, w, W):
    candidates = set()
    n = len(v)
    for i in range(n):
        candidates.add(i)

    sol = [0] * n
    weight = 0
    while candidates and weight < W:
        best = get_best_item(candidates, v, w)
        candidates.remove(best)
        if w[best] + weight <= W:
            sol[best] = 1 * v[best]
            weight += w[best]
        else:
            sol[best] = ((W-weight) / w[best]) * v[best]
            weight = W
    return sol


def main() -> None:
    n, m = map(int, input().split())
    values = []
    weights = []
    for i in range(m):
        v, p = map(int, input().split())
        values.append(v)
        weights.append(p)
    algorithm = sum(greedy_knapsack(values, weights, n))

    print("{:.2f}".format(algorithm))


if __name__ == '__main__':
    main()