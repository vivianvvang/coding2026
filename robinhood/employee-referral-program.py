from collections import defaultdict
import heapq
def empRefProgram(referrers, referrals):
    graph = defaultdict(list)

    for referrer, referaral in zip(referrers, referrals):
        graph[referrer].append(referaral)

    heap = []
    roots = set(referrers) - set(referrals)
    referral_counts = {}

    def dfs(root):
        if root not in graph:
            return 0
        sum = 0
        for neighbor in graph[root]:
            sum += dfs(neighbor) + 1
        referral_counts[root] = sum
        return sum

    for r in roots:
        count = dfs(r)

    for r, count in referral_counts.items():
        heapq.heappush(heap, (-count, r))

    res = []
    for _ in range(3):
        count, node = heapq.heappop(heap)
        res.append(f"{node} {-count}")
    return res

referrers = ["A", "A", "B", "C"]
referrals = ["B", "C", "D", "E"]
print(empRefProgram(referrers, referrals))
