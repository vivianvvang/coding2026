from typing import List, Optional

class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        # TODO: Implement wordSearch logic
        m, n = len(board), len(board[0])
        visited = set()

        def search(i, j, depth, dx, dy):
            if depth == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != word[depth]:
                return False

            res = False
            visited.add((i, j))
            res = search(i + dx, j + dy, depth + 1, dx, dy) 
            visited.remove((i, j))
            
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res = False
                    for dx, dy in dirs:
                        if search(i, j, 0, dx, dy):
                            return True
        return False
