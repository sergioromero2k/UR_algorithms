import heapq

def dijkstra(g, start):
    distances = [0x3f3f3f3f] * len(g)
    distances[start] = 0
    q = [(0, start)]
    while q:
        curr_distance, curr_node = heapq.heappop(q)
        if distances[curr_node] <= curr_distance:
            for neighbor, w in g[curr_node]:
                distance = curr_distance + w
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(q, (distance, neighbor))
    return distances

def solve(g, types, n_types):
    solution = [0x3f3f3f3f] * n_types
    for v in range(len(g)):
        distances = dijkstra(g, v)
        for u in range(len(distances)):
            if u != v and types[u] == types[v]:
                solution[types[v]] = min(solution[types[v]], distances[u])


def main() -> None:
    n, m = map(int, input().strip().split())
    types = list(map(int, input().strip().split()))
    g = []

    types_set = set()
    for i in range(n):
        g.append([])
        types_set.add(types[i])

    for _ in range(n):
        g.append([])

    for _ in range(m):
        u, v, c= map(int, input().strip().split())
        g[u].append((v,c))
        g[v].append((u,c))
    sol = solve(g, types, len(types_set))
    for s in sol:
        print(f"{s} ")
