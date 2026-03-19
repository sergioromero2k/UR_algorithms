#!/usr/bin/env python3

def main() -> None:
    n,m = map(int, input().strip().split())
    grafo = list()
    i = 0

    for _ in range(n):
        grafo.append([])
    for _ in range(n):
        h1, h2 = map(int, input().strip().split())
        grafo[h1].append(h2)

    print("\n")
    print(grafo)

if __name__ == "__main__":
    main()