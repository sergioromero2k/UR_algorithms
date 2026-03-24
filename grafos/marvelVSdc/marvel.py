#!/dev/bin/python3

def main() -> None:
    n, m, p = input().strip().split()
    n = int(n)
    m = int(m)

    selection = [[] for _ in range(n)]
    for _ in range(n):
        selection.append(input().strip())

    for _ in range(m):
        a, b = map(int, input().strip().split())





if __name__ == "__main__":
    main()