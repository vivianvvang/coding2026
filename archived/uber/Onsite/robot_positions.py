from typing import List

class Solution:
    def findRobotsPosition(self, board: List[List[str]], distance: List[int]) -> List[List[int]]:
        # TODO: Implement findRobotsPosition logic
        L, T, B, R = 0, 1, 2, 3

        if not board or not board[0] or len(distance) != 4:
            return []
        
        r, c = len(board), len(board[0])
        res = []
        map_ = {}

        # initialization
        top = [-1] * c # Last seen 'X' row index in each column (from top)
        bottom = [r] * c # Last seen 'X' row index in each column (from bottom)

        # first pass: row by row, left to right, compute left and top
        for i in range(r):
            left = -1 # track the most recent 'X' in current row
            for j in range(c):
                if board[i][j] == 'O':
                    dl = abs(j - left)
                    dt = abs(i - top[j])
                    map_[f"{i},{j}"] = [dl, dt, -1, -1]
                if board[i][j] == 'X':
                    left = j #update left blocker
                    top[j] = i # update i column's top blocker as i

        # second pass: bottom to top, right to left
        for i in range(r-1, -1, -1):
            right = c
            for j in range(c-1, -1, -1):
                if board[i][j] == 'O':
                    db = abs(i - bottom[j])
                    dr = abs(right - j)

                    key = f"{i},{j}"
                    if key in map_:
                        curr_d = map_[key]
                        curr_d[B] = db
                        curr_d[R] = dr
                        if (curr_d[L] == distance[L] and
                            curr_d[T] == distance[T] and
                            curr_d[B] == distance[B] and
                            curr_d[R] == distance[R]):
                            res.append([i, j])
                if board[i][j] == 'X':
                    right = j
                    bottom[j] = i
        return res