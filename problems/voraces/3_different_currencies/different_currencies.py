#!/usr/bin/env python3
from math import ceil


def money_exchange(value, coins):
    """
    Calculates the distribution of denominations for a given value.
    Returns a list of counts corresponding to the 'coins' list.
    """
    exchange = exchange = [0] * len(coins)
    i = 0
    while i < len(coins) and value > 0:
        exchange[i] = value // coins[i]
        value = value % coins[i]
        i += 1
    return exchange


def main() -> None:
    """
    Handles data input, currency storage, and processes transactions.
    Outputs all results at the end for a clean display.
    """
    try:
        cash_on_hand = int(input())
        if not cash_on_hand:
            return
        total_cash = int(input())
        if not total_cash:
            return

        if 1 <= total_cash <= 3:
            currencies = {}
            for _ in range(total_cash):
                n_money = input().split()
                if len(n_money) == 0:
                    raise Exception(
                        "Introduce data error.\n Program finished.")

                name = n_money[0]
                change = float(n_money[1])
                # Verification if sorted moneys.
                currency_list = sorted(
                    [int(x) for x in n_money[2:]], reverse=True)
                currencies[name] = [change, currency_list]
        else:
            raise Exception(
                "Past limit in total cash .\n Program finished.")

        n_purchases = int(input())
        if not n_purchases:
            raise Exception(
                "Introduce data error.\n Program finished.")

        results_to_print = []
        if 2 <= n_purchases <= 4:
            for i in range(1, n_purchases + 1):
                coins_pay = input().split()
                if len(coins_pay) == 0:
                    raise Exception(
                        "Introduce data error.\n Program finished.")

                name = coins_pay[0]
                customer_spending = int(coins_pay[1])

                if name not in currencies:
                    raise Exception(
                        "Introduce data error.\n Program finished.")

                euro_amount = currencies[name][0]
                changes_available = currencies[name][1]

                result_counts = money_exchange(
                    customer_spending, changes_available)
                payment_str = []
                for idx in range(len(result_counts)):
                    count = result_counts[idx]
                    coin_value = changes_available[idx]
                    for _ in range(count):
                        payment_str.append(str(coin_value))

                results_to_print.append(
                    f"Pedido {i} paga con {' '.join(payment_str)}")
                cash_on_hand += ceil(customer_spending * euro_amount)
        else:
            raise Exception("Past limit in total cash .\n Program finished.")

        for linea in results_to_print:
            print(linea)
        print(f"Dinero al final del dia: {cash_on_hand}")

    except ValueError as e:
        print("Value Error", e)
    except Exception as e:
        print("Value Error", e)


if __name__ == "__main__":
    main()
