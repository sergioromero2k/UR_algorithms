import sys


def binary_search(v, limit):
    low = 0
    high = len(v) - 1
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if v[mid] <= limit:
            result = mid + 1
            low = mid + 1
        else:
            high = mid - 1
    return result


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    lines = [l for l in lines if l.strip()]

    spoderman = list(map(int, lines[0].split()))
    rastaman = list(map(int, lines[1].split()))
    n = int(lines[2].strip())

    for i in range(n):
        s, r = map(int, lines[3 + i].split())
        cs = binary_search(spoderman, s)
        cr = binary_search(rastaman, r)
        print(cs, cr)
        if cs > cr:
            print("SPODERMAN")
        elif cr > cs:
            print("RASTAMAN")
        else:
            print("EMPATE")