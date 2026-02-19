#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int: 
        um = defaultdict(list) 
        for pair in connections:
            l, r= pair[0], pair[1]
            um[l].append((r, 1)) # direction need to be reversed
            um[r].append((l, 0))
        ans = 0
        visited = set()
        
        def dfs(graph, start, visited):
            nonlocal ans
            visited.add(start)
            for node, direction in graph.get(start):
                if node not in visited:
                    ans += direction
                    dfs(graph, node, visited)
            return visited

        dfs(um, 0, visited)
        return ans
        


# @lc code=end

