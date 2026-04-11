#!/usr/bin/env python3

def get_best_item(n, names, spaces, values):
    """Finds the index of the candidate with the highest talent/space ratio"""
    best_item = -1
    best_ratio = -1
    for i in range(len(names)):
        if spaces[i] > 0:
            ratio = values[i] / spaces[i]
            if ratio > best_ratio:
                best_ratio = ratio
                best_item = i
    return best_item


def greedy_knapsack(n, names, spaces, talents, capacity):
    """Fills a single room maximizing talent using a greedy algorithm"""
    talent_total = 0.0
    chosen = []

    continua = True
    while capacity > 0 and continua:
        best = get_best_item(n, names, spaces, talents)

        if best != -1:
            chosen.append(names[best])

            # Case: Candidate fits entirely
            if spaces[best] <= capacity:
                talent_total += talents[best]
                capacity -= spaces[best]
                spaces[best] = 0
            # Case: Fractional fit (body at the door)
            else:
                fraction = capacity / spaces[best]
                talent_total += talents[best] * fraction

                # Update remaining space and talent for next rooms
                spaces[best] -= capacity
                talents[best] -= talents[best] * fraction
                capacity = 0
        else:
            continua = False

    return talent_total, chosen


def main() -> None:
    try:
        line = input()
        if not line: return
        entrance_n = int(line)

        names = []
        spaces = [0.0] * entrance_n
        t1 = [0.0] * entrance_n
        t2 = [0.0] * entrance_n
        t3 = [0.0] * entrance_n

        # Load all candidates first
        if 10 <= entrance_n <= 1000:
            for i in range(entrance_n):
                data = input().split()
                if not data: break
                names.append(data[0])
                spaces[i] = float(data[1])
                t1[i] = float(data[2])
                t2[i] = float(data[3])
                t3[i] = float(data[4])
            # Load room capacities
            line_caps = input().split()
            if not line_caps: return
            caps = list(map(int, line_caps))

            list_talents = [t1, t2, t3]

            # Process each of the 3 rooms sequentially
            for i in range(3):
                talent_h, chosen_h = greedy_knapsack(entrance_n, names, spaces, list_talents[i], caps[i])

                print("HABITACION {}: {:.2f}".format(i, round(talent_h, 2)))
                for name in chosen_h:
                    print(name)
        else:
            raise Exception("Limits")
    except ValueError:
        print("INVALID INPUT")
        return
    except Exception as e:
        print("Error", e)
        return

if __name__ == "__main__":
    main()
