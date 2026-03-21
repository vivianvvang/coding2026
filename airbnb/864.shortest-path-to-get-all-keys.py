#
# @lc app=leetcode id=864 lang=python3
#
# [864] Shortest Path to Get All Keys
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys = set()
        visited = set() 
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()
        min_steps = float('inf')
        
        # add starting point and find all keys
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '@':
                    # in q, save (coordinates, keys, steps) as a combined state
                    q.append((i, j, "", 0))
                    visited.add((i, j, ""))
                elif grid[i][j] >= 'a' and grid[i][j] <= 'k':
                    keys.add(grid[i][j])
        
        # state-space bfs
        while len(q) > 0:
            r, c, k_status, step = q.popleft()
            # should not visit same state twice 
            # if (r, c, k_status) in visited:
            #     continue
            # visited.add((r, c, k_status))
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                n_status = k_status
                if nr < 0 or nr >= m or nc < 0 or nc >= n: # off board
                    continue
                value = grid[nr][nc]
                
                # wall
                if value == '#': 
                    continue
                # lock with no keys
                if value >= 'A' and value <= 'K' and value.lower() not in k_status: 
                    continue
                
                if value >= 'a' and value <= 'k':
                    keys.add(value)
                    n_status = "".join(sorted(k_status + value)) if value not in k_status else k_status
                    if len(n_status) == len(keys): 
                        return step + 1
                        # BFS guarantees that the first time we reach any state, it is via the shortest possible path

                if (nr, nc, n_status) in visited:
                    continue
                visited.add((nr, nc, n_status))
                q.append((nr, nc, n_status, step + 1))

        return min_steps if min_steps != float('inf') else -1
        
# Time Complexity: O(m * n * 2^k)
        
# @lc code=end

