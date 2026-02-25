#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        len_grid = len(grid)
        start, end = 0, len_grid * len_grid -1
        uf = UnionFind(len_grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for t in range(grid[0][0], len_grid * len_grid):
            q = deque()
            v = set()
            q.append(0)
            v.add(0)
            while q:
                node = q.popleft()
                x, y = node // len_grid, node % len_grid
                for dir in dirs:
                    nx, ny = x + dir[0], y + dir[1]
                    flatten_n = self.flatten(nx, ny, len_grid)
                    
                    if self.in_bound(len_grid, nx, ny) and flatten_n not in v:
                        v.add(flatten_n)
                        if grid[nx][ny] <= t:
                            uf.union(node, flatten_n)
                            q.append(flatten_n)
                    if uf.find(start) == uf.find(end):
                        return t

        return t
 
    def flatten(self, x, y, n) -> int:
        return x * n + y
    
    def in_bound(self, n, x, y) -> bool:
        return x >= 0 and y >= 0 and x < n and y < n
        
# @lc code=end
class UnionFind:
    def __init__(self, len_grid):
        n = len_grid * len_grid
        self.parent = list(range(n))
        self.height = [1] * n
    
    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False 
    
        # union by height: attach smaller tree to larger tree
        if self.height[root_x] > self.height[root_y]:
            self.parent[root_y] = root_x
        elif self.height[root_x] < self.height[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.height[root_x] += 1
        return True   