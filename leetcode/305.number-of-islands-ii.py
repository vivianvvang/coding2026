#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#

# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.count = 0 #ans
        self.parent = [-1] * n
        self.height = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        
        if self.height[rx] > self.height[ry]:
            self.parent[ry] = rx
        elif self.height[ry] > self.height[rx]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            self.height[rx] += 1
        # island count change
        self.count -= 1
        return True

class Solution:

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def isLand(x, y, m, n):
            return x >= 0 and y >= 0 and x < m and y < n
    
        def flatten(x, y, m, n) -> int:
            return x * n + y
        
        res = []
        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        uf = UnionFind(m * n)
        
        for x, y in positions:
            idx = flatten(x, y, m, n)
            if uf.parent[idx] != -1:
                res.append(uf.count)
                continue
            
            # turn into land
            uf.parent[idx] = idx  
            uf.count += 1

            # union
            for dir_x, dir_y in dirs:
                nx, ny = x+dir_x, y+dir_y
                nidx = flatten(nx, ny, m, n)
                if isLand(nx, ny, m, n) and uf.parent[nidx] != -1:
                    uf.union(idx, nidx)
            res.append(uf.count)
        
        return res
        
# @lc code=end

