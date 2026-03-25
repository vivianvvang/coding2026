'''
7. 一道dfs，player根据当前cell值（J, W）可以跳格子或走格子，问能不能到终点。
follow-up是最短路径。

# boardJump
walk_movements = [
	(0, 1),
	(0, -1),
	(1, 0),
	(-1, 0),
]
jump_movements = [
	(0, 2),
	(0, -2),
	(2, 0),
	(-2, 0)
]

board = [
	['J', 'W', 'W'],
	['W', 'J', 'W'],
	['J', 'W', 'J'],
]
'''

from collections import deque

def boardJump(board):
    m, n = len(board), len(board[0])
    target = (m - 1, n - 1)  # target
    walk_movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    jump_movements = [(0, 2), (0, -2), (2, 0), (-2, 0)]

    q = deque([(0, 0, 0)])
    visited = set()
    visited.add((0, 0))

    while q:
        x, y, steps = q.popleft()
        if (x, y) == target:
            return True, steps
        val = board[x][y]
        dirs = jump_movements if val == "J" else walk_movements
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                q.append((nx, ny, steps + 1))
                visited.add((nx, ny))
    return False, -1
board = [
    ['J', 'W', 'W'],
    ['W', 'J', 'W'],
    ['J', 'W', 'J'],
]
can_reach, shortest_path = boardJump(board)
print(can_reach)
print(shortest_path)