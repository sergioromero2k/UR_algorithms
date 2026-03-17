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
    sele = []
    no_sele = []
    accum = 0
    for task in sol:
        accum += tasks[task]
        if accum <= m:
            sele.append(accum)
        else:
            no_sele.append(accum)
    return sele, no_sele


def main() ->None:
    n, m = map(int, input().split())
    candidates = list()
    tasks = list()
    for _ in range(n):
        s, t = input().split()
        t = int(t)
        candidates.append((s, t))
        tasks.append((t))
    sol = order_task(tasks)
    print("Seleccionadas:")
    i= 0
    times = calculate_waiting_time(sol, tasks)

    total = 0
    while i < len(sol) and times[i] <= m:
        idx = sol[i]
        name, time = candidates[idx]
        print(name)
        i += 1

    print("No seleccionadas:")
    while i < len(sol):
        idx = sol[i]
        name, time = candidates[idx]
        print(name)
        i += 1

    total = times[i - 2]
    print(total)

if __name__ == '__main__':
    main()




























