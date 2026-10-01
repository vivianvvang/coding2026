from typing import List, Optional
from collections import deque, defaultdict

class Solution:
    def maxMultiplierProduct(self, n: int, edges: List[List[int]], start: int, end: int) -> int:
        graph = defaultdict(list)
        for s, e, w in edges:
            graph[s].append((e, w))
                
        def dfs(curr, visited, end):
            if curr == end:
                return 1
            visited.add(curr)
            res = -1

            for next, w in graph[curr]:
                if next not in visited:
                    future = dfs(next, visited, end)
                    if future != -1:
                        res = max(res, w * future)
            visited.remove(curr)
            return res
        
        ans = dfs(start, set(), end)

        return ans if ans != -1 else -1
