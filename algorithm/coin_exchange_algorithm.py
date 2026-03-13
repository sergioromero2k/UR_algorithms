#!/usr/bin/env python3

def money_exchange(value, coins):
    exchange = [0] * len(coins)
    i = 0
    while i < len(coins) and value > 0:
        exchange[i] = value // coins[i]
        value = value % coins[i]
        i += 1
    return exchange


def main() -> None:
    coins = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    value = 4
    exchange = money_exchange(value, coins)
    print(exchange)

if __name__ == '__main__':
    main()