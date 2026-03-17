#!/usr/bin/env python3

def get_best_item(candidates, profit):
    best_item = -1
    best_profit = -1
    for c in candidates:
        if profit[c] > best_profit:
            best_profit = profit[c]
            best_item = c
        return best_item

def greedy_schedule(profit, deadline):
    n = len(profit)
    candidates = set()
    for i in range(n):
        candidates.add(i)
    last_date = max(deadline)
    sol = [-1] * (last_date + 1)
    j = 0
    while candidates and j <= last_date:




def main() -> None:
    pass

if __name__ == '__main__':
    main()