class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.height = [1] * n # 2. Rank: Height of the tree (for balancing)
        self.count = n # Optional: Track count of components
        
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False # already connected
        
        # union by height: attach smaller tree to larger tree
        if self.height[root_x] > self.height[root_y]:
            self.parent[root_y] = root_x
        elif self.height[root_x] < self.height[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.height[root_x] += 1
        self.count += 1
        return True 