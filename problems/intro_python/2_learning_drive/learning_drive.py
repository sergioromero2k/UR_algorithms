#!/usr/bin/env python3

def main() -> None:

    instruction = {
        "Arranca": "Mete primera y pisa acelerador",
        "Cambia de marcha": "Pisa embrague a fondo",
        "Para": "Pisa freno y embrague",
        "Aparca": "Imposible",
        "Rotonda": "POR EL CARRIL DERECHO",
        "Gira": "El intermitente, por favor"
    }

    try:
        entrance = input().strip()
        if not entrance:
            return
        n = int(entrance)
        if 1 <= n <= 100:
            for _ in range(n):
                situation = input().strip()
                if not situation:
                    return
                if situation in instruction:
                    print(instruction[situation])
        else:
            raise Exception("Error limits")
    except ValueError as e:
        print("Invalid entrance: ", e)
    except Exception as e:
        print("Error", e)


if __name__ == '__main__':
    main()



"""
# Other forms, but it need python > 3.10
def main() -> None:

    instruction = {
        "Arranca": "Mete primera y pisa acelerador",
        "Cambia de marcha": "Pisa embrague a fondo",
        "Para": "Pisa freno y embrague",
        "Aparca": "Imposible",
        "Rotonda": "POR EL CARRIL DERECHO",
        "Gira": "El intermitente, por favor"
    }

    try:
        entrance = input().strip()
        if not entrance:
            return
        n = int(entrance)
        if 1 <= n <= 100:
            for _ in range(n):
                situation = input().strip()
                if not situation:
                    return
                if situation in instruction:
                    print(instruction[situation])
        else:
            raise Exception("Error limits")
    except ValueError as e:
        print("Invalid entrance: ", e)
    except Exception as e:
        print("Error", e)


if __name__ == '__main__':
    main()
"""