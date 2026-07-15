import heapq
from collections import defaultdict
def min_eta(n, edges, s, t):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    
    dists = [float("inf")] * n
    dists[s] = 0
    heap = [(0, s)]
    while heap:
        curr, node = heapq.heappop(heap)
        if curr != dists[node]:
            # Skip stale heap entries
            # In Dijkstra, the same node may be pushed into the heap multiple times with different distances.
            continue

        if node == t:
            return curr
        for neighbor, weight in graph[node]:
            new_dist = curr + weight
            if new_dist < dists[neighbor]:
                dists[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return -1

n = 5
edges = [
    (0, 1, 2),
    (0, 2, 5),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 1),
    (3, 4, 3),
]
print(min_eta(n, edges, 0, 4) == 7)