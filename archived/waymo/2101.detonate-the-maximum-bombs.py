#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#
from collections import deque, defaultdict

# @lc code=start
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= ri ** 2:
                    adj[i].append(j)
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= rj ** 2:
                    adj[j].append(i)
        
        
        ans = 1

        for i in range(n):
            visited = set()
            q = deque([i])
            visited.add(i)
            tmp = 0
            while len(q) > 0:
                idx = q.popleft()
                tmp += 1
                for nei in adj[idx]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            ans = max(ans, tmp)
        
        return ans
                    

            
        
# @lc code=end

