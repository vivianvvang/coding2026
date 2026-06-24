#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        q = deque([(0, 0, 1)])
        grid[0][0] = 1
        while len(q) > 0:
            x, y, steps = q.popleft()
            if x == m - 1 and y == n - 1:
                return steps
            for dir in dirs:
                nx, ny = x + dir[0], y + dir[1]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 0:
                    q.append((nx, ny, steps + 1))
                    grid[nx][ny] = 1
        return -1
# @lc code=end

