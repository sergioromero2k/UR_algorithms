#!/usr/bin/env python3

def greedy_scheduler(candidates: list):
    """Greedy scheduling to maximize total temptation."""

    # Sort candidates by temptation (highest first)
    candidates.sort(key=lambda x: -x[2])

    # Maximum possible day
    max_day = max(c[1] for c in candidates) if candidates else 0

    # Schedule possible day
    schedule = [None] * (max_day + 1)

    # Try to place each candidate on the latest free day ≤ limit
    for name, limit, attraction in candidates:
        assigned = False
        day = limit
        while day >= 0 and not assigned:
            if schedule[day] is None:
                schedule[day] = (name, limit)
                assigned = True
            day -= 1
    return schedule


def main() -> None:
    """
    Read input, run scheduler, print results.
    Constraint 4 ≤ N ≤ 100 is assumed valid (not checked).
    """
    try:
        n = input().strip()
        if not n: return
        n = int(n)

        candidates = []
        # Read candidates: name, max day, temptation
        for _ in range(n):
            parts = input().strip().split()
            if not len(parts) == 3: return
            candidates.append((parts[0], int(parts[1]), int(parts[2])))

        final_schedule = greedy_scheduler(candidates)

        for day, entry in enumerate(final_schedule):
            if entry:
                name, limit = entry
                remaining = limit - day
                print(f"DIA {day}: {name}, LE SOBRAN {remaining} DIAS")
            else:
                print(f"DIA {day}: SIN TENTADOR")

    except (ValueError, EOFError) as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
