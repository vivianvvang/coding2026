#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for i, j in len(grid), len(grid[0]):
            if grid[i][j] == '1' and (i, j) not in visited:
                count += 1
                self.dfs(grid, i, j, visited)
        return count
    
    def dfs(self, grid, i, j, visited):
        if grid[i][j] == '1' or (i, j) in visited:
            return
        visited.add((i, j))
        if i + 1 < len(grid):
            self.dfs(self, grid, i+1, j, visited)
        if i -1 >= 0:
            self.dfs(self, grid, i-1, j, visited)
        if j + 1 < len(len(grid)):
            self.dfs(self, grid, i, j+1, visited)
        if j -1 >= 0:
            self.dfs(self, grid, i, j-1, visited)



        
# @lc code=end

