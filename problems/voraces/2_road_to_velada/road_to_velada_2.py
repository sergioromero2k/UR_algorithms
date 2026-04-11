#!/usr/bin/env python3
"""
Greedy algorithm to solve the Activity Selection Problem.
Optimized for competitive programming and automated grading.
"""

def greedy_select_activity(start, end) -> list:
    activities = list(zip(start, end, range(len(end))))
    activities.sort(key=lambda x:x[1])
    result =[]
    last_end = -1
    for a in activities:
        if a[0] >= last_end:
            result.append(a[2])
            last_end = a[1]
    return result


def main() -> None:
    try:
        N: int = int(input())
        if not N: return
        if 5 <= N <= 10 :
            start = []
            end = []
            for _ in range(N):
                activity = input()
                if not activity: return
                activity = activity.split()
                if len(activity) == 3:
                    start_act = int(activity[1])
                    end_act = int(activity[2])
                    if 0 <= start_act <= end_act <= 10000:
                        start.append(int(start_act))
                        end.append(int(end_act))
                    else:
                        return
                else:
                    return
            result = greedy_select_activity(start, end)
            print(len(result))
        else:
            raise Exception("Limits of N")
    except ValueError as e:
        print("Value Error: ", e)
        return
    except Exception as e:
        print("Error: ", e)
        return
    
    
if __name__ == "__main__":
    main()
