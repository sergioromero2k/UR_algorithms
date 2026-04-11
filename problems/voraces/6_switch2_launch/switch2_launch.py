#!/usr/bin/env python3

"""
def main() -> None:
    n = input().strip()
    if not n: return
    n = int(n)

    queue = []

    for _ in range(n):
        p = int(input().strip())
        for i in range(p):
            person = input().strip().split()
            if len(person) == 2:
                c, t = person
                queue.append((str(c), int(t)))

    queue.sort(key=lambda a : a[1])
    name_order = [name[0] for name in queue]

    print(" ".join(name_order))

    time_total = 0
    accumulated = 0

    for _, t in queue:
        accumulated += t
        time_total += accumulated

    print(time_total)


if __name__ == "__main__":
    main()
"""


def min_wait_algorithm(list_person: list) :
    """Sorts user by time (SJF) and calculates total completion time."""
    # Sort by time (T to minimize the waiting sequence).
    list_person.sort(key=lambda a : a[1])

    name_order: list = []
    accumulated: int = 0
    time_total: int = 0

    for name, time in list_person:
        name_order.append(name)
        accumulated += time
        time_total += accumulated

    return name_order, time_total


def main() -> None:
    """Handles N queues and manages input/output formatting."""
    try:
        n = input().strip()
        if not n: return
        n_queue = int(n)
        # Constraint check for number of queues
        if not (1 <= n_queue <= 20): return

        for _ in range(n_queue):
            p = input().strip()
            if not p: return
            p_person = int(p)

            # Constraint check for people per queue
            if not (3 <= p_person <= 40): return
            data_queue = []

            for _ in range(p_person):
                line = input().strip().split()
                if not line or len(line) != 2: return

                name, time = line
                data_queue.append((str(name), int(time)))

            names, result_times = min_wait_algorithm(data_queue)

            print(" ".join(names))
            print(result_times)

    except (EOFError, ValueError) as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
