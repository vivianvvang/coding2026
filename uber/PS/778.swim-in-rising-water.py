import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # keep a priority queue of which square we can walk in next. 
        # We always walk in the smallest one that is 4-directionally adjacent to ones we've visited.
        n = len(grid)
        hq = [(grid[0][0], (0, 0))] # starting point
        visited = set((0, 0))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def in_bound(x, y) -> bool:
            return x >= 0 and y >= 0 and x < n and y < n
        
        while hq:
            t, coor = heapq.heappop(hq)
            if coor == (n-1, n-1):
                return t
            
            for dir in dirs:
                nx, ny = coor[0] + dir[0], coor[1] + dir[1]
                if in_bound(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    next_t = max(t, grid[nx][ny])
                    heapq.heappush(hq, (next_t, (nx, ny)))
        return -1
    
    # O(N^2logN). We may expand O(N^2) nodes, 
    # and each one requires O(logN) to perform heap operations