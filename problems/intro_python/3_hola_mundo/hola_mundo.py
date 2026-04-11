#!/usr/bin/env python3

def main():
    entrance = int(input())
    if not entrance:
        return
    try:
        if 1 <= entrance <= 50:
            for i in range(entrance):
                print("¡Hola mundo!")
    except ValueError as e:
        print("El tipo de dato es incorrecto")

if __name__ == "__main__":
    main()
