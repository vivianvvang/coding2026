#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import List

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])
        visited = set()
        def search(visited, i, j, depth):
            if depth == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != word[depth]:
                return False
            res = False
            visited.add((i, j))
            
            for dx, dy in d:
                x, y = dx + i, dy + j
                res = search(visited, x, y, depth + 1) or res
            visited.remove((i, j))
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    ans = search(visited, i, j, 0)
                    if ans == True:
                        return ans
        return False
        
# @lc code=end

