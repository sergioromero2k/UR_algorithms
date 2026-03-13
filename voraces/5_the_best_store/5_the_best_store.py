#!/usr/bin/env python3

def money_exchange(value, coins):
    mini_money  = float('inf')
    exchange = [0] * len(coins)
    i = 0
    while i < len(coins) and value > 0:
        if value >= coins[i]:
            mini_money = coins[i]
            exchange[i] = value // coins[i]
            value = value % coins[i]
        i += 1
    return mini_money, value


def main() -> None:
    try:
        n = int(input())
        d = float(input())
    except EOFError:
        return
    results = []
    for i in range(n):
        o = input()
        coins = input()
        coins = list(map(int, coins.split()))
        coins.sort(reverse=True)
        exchange, value = money_exchange(d, coins)
        results.append((o, value, exchange))

    best_store_name = ""
    best_money_value = float('inf')
    for o, v, e in results:
        if v > 0:
            print(f"{o} me debe {v} euro")
            best_money_value = e
            best_store_name = o
        if v == 0:
            if e <= best_money_value:
                best_money_value = e
                best_store_name = o
    if best_store_name:
        print(f"La mejor tienda es {best_store_name} me devuelven monedas de {best_money_value:g}")
if __name__ == "__main__":
    main()


