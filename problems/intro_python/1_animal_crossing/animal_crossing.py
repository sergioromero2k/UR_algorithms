#!/usr/bin/env python3

def main() -> None:
    """Exercise of ordering the best option and second-best option"""
    try:
        entrance_c = input().strip()
        if not entrance_c:
            return

        c = int(entrance_c)

        numbers = []
        if 10 <= c <= 1000:
            for _ in range(c):
                data = input().split()
                if len(data) == 2:
                    idx = int(data[0])
                    value = int(data[1])
                    numbers.append((idx, value))

            numbers.sort(key=lambda n: n[1], reverse=True)
            best = numbers[0]
            second_best = numbers[1]

            sum_best = best[1] + second_best[1]
            print(f"{best[0]} {second_best[0]} {sum_best}")
        else:
            raise Exception("Limits of range.")

    except ValueError as e:
        print("Value Error: ", e)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
