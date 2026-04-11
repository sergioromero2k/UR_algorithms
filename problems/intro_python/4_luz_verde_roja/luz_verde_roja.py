#!/usr/bin/env python3

def main() -> None:
    """Function implements a game of light green and red"""
    try:
        entrance = input()
        data = entrance.split(' ')
        data_formatted = [item.strip() for item in data]
        entrance_n = int(data_formatted[0])
        entrance_c = data_formatted[1]
        entrance_a = int(data_formatted[2])
        result = "JUGADOR "

        if 0 <= entrance_n <= 999:
            if 0 <= entrance_n <= 9:
                result += "00"
            elif 0 <= entrance_n <= 99:
                result += "0"
            result += str(entrance_n)
            if entrance_c == "r" and entrance_a == 1:
                result += " ELIMINADO"
            else:
                result += " CONTINUAR"
            print(result)
        else:
            raise Exception("Error: Limits: ", entrance_n)
    except ValueError as e:
        print("Error: Type data: ", e)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
