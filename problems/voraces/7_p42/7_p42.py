#!/usr/bin/en python3

def get_best_task(candidates, tasks):
    best_task = 0
    best_time_task = 0x3f3f3f3f
    for c in candidates:
        if tasks[c] < best_time_task:
            best_time_task = tasks[c]
            best_task = c
    return best_task

def order_task(tasks):
    candidates = set()
    for i in range(len(tasks)):
        candidates.add(i)

    sol = []
    while candidates:
        best = get_best_task(candidates, tasks)
        candidates.remove(best)
        sol.append(best)
    return sol

def calculate_waiting_time(sol, tasks, m):
    time = []
    accum = 0
    total = 0
    sele = []
    sele_no = []
    for idx in sol:
        if total < m:
            accum += tasks[idx]
            time.append(accum)
            sele.append(idx)
            total = sum(time)
        else:
            sele_no.append(idx)
    return sele, sele_no, total


def main() -> None:
    n, m = map(int, input().split())
    candidates = list()
    tasks = list()
    for _ in range(n):
        s, t = input().split()
        t = int(t)
        candidates.append((s, t))
        tasks.append(t)

    sol = order_task(tasks)
    sele, sele_no, total = calculate_waiting_time(sol, tasks, m)

    print("Seleccionadas:")
    for idx in sol:
        if idx in sele:
            print(candidates[idx][0])

    print("No seleccionadas:")
    for idx in sol:
        if idx in sele_no:
            print(candidates[idx][0])
    print(total)


if __name__ == '__main__':
    main()




























