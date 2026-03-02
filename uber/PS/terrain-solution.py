class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]


# $O(MN log MN)
class TerrainSolution:
    def solution(self, terrain, limits):
        # 1. pre-processing
        m, n = len(terrain), len(terrain[0])
        cells = []
        
        for r in range(m):
            for c in range(n):
                cells.append((terrain[r][c], r, c))
        cells.sort()
        cell_idx = 0

        # 2. sort by value of limit
        sorted_queries = sorted(enumerate(limits), key =  lambda x: x[1])

        uf = UnionFind(m * n)
        active = [[False] * n for _ in range(m)]
        results = [0] * len(limits)

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # 3. connect, from limit small to big
        for limit_idx, limit in sorted_queries:

            # skip idx < cell_idx
            while cell_idx < len(cells) and cells[cell_idx][0] < limit:
                # connect cell with its neighbors
                val, r, c = cells[cell_idx]
                active[r][c] = True

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and active[nr][nc]:
                        uf.union(r * n + c, nr * n + nc)
                cell_idx += 1
            
            if terrain[0][0] < limit:
                rt = uf.find(0)
                results[limit_idx] = uf.size[rt]
            else:
                results[limit_idx] = 0
        return results


solution = TerrainSolution()
terrain = [[1,2,10], [1,5,10], [1,1,1]]
limits = [2, 4, 6]
print(solution.solution(terrain, limits))