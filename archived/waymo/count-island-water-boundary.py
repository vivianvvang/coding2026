
def landAreasAndBoundaries(grid):
    visited = set()
    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = []

    def dfs(i, j, water):
        if (i, j) in visited or grid[i][j] == 0:
            return 0
        visited.add((i, j))
        area = 1
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni >= 0 and nj >= 0 and ni < m and nj < n:
                if grid[ni][nj] == 0:
                    water.add((ni, nj))
                elif (ni, nj) not in visited:
                    area += dfs(ni, nj, water)
        return area
                    

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in visited:
                water = set()
                land_area = dfs(i, j, water)
                res.append([land_area, len(water)])
    return res


grid = [[1, 1, 0, 0, 0], [1, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 1, 0, 0]]
print(landAreasAndBoundaries(grid))