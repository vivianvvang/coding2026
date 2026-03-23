
from collections import deque

def calculate(board):
    graph = []
    for s in board:
        graph.append(s.split(" "))
    
    m, n = len(graph), len(graph[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = 0

    for i in range(m):
        for j in range(n):
            if graph[i][j] != '#':
                tile = graph[i][j][0]
                q = deque()
                q.append((i, j))
                area, crowns = 1, int(graph[i][j][1:])
                graph[i][j] = "#"
                
                # BFS
                while len(q) > 0:
                    x, y = q.popleft()
                    
                    for dir in range(len(dirs)):
                        dx, dy = dirs[dir][0], dirs[dir][1]
                        nx, ny =  x + dx, y + dy
                        if nx >= 0 and nx < m and ny >= 0 and ny < n and graph[nx][ny][0] == tile:
                            print(nx, ny, graph[nx][ny])
                            area += 1
                            crowns += int(graph[nx][ny][1:])
                            graph[nx][ny] = "#"
                            q.append((nx, ny))
                res += area * crowns
                print(tile, area, crowns)
    return res
  

board = ["L0 W1 W1 W0 F2",
         "W0 W0 T0 T0 T0",
         "W0 W1 T0 R2 R1" ,
         "L0 K0 L1 L0 L0",
         "R0 C2 C0 L1 T0"]
print(calculate(board))



