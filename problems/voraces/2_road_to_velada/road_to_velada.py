#!/usr/bin/env python3
"""
Greedy algorithm to solve the Activity Selection Problem.
Optimized for competitive programming and automated grading.
"""

def greedy_select_activity(start, end) -> int:
    """
    Select the maximum number of non-overlapping activities.
    Returns the count of selected activities.
    """
    activities = list(zip(start, end))
    activities.sort(key=lambda x:x[1])

    count = 0
    last_end = -1

    for s, e in activities:
        if s >= last_end:
            count += 1
            last_end = e
    return count


def main() -> None:
    try:
        line = input()
        if not line: return
        line = int(line)
        start = []
        end = []
        for _ in range(line):
            activity = input()
            if not activity: return
            activity = activity.split()
            start_act = int(activity[-2])
            end_act = int(activity[-1])
            start.append(int(start_act))
            end.append(int(end_act))
        result = greedy_select_activity(start, end)
        print(result)
    except ValueError as e:
        print("Value Error: ", e)
        return
    except Exception as e:
        print("Error: ", e)
        return
    
    
if __name__ == "__main__":
    main()
