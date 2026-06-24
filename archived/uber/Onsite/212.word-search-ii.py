from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        def _insert(word):
            current = trie
            for ch in word:
                if ch not in current:
                    current[ch] = {}
                current = current[ch]
            current['#'] = word
        # insert all words into a trie
        for word in words:
            _insert(word)

        m, n = len(board), len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = []

        def _backtrack(x, y, current):
            if x < 0 or y < 0 or x >= m or y >= n:
                return
            if board[x][y] == '#':
                return
            ch = board[x][y]
            # return if there's no such word
            if ch not in current:
                return
            
            current = current[ch]
            word_found = current.pop('#', None)
            if word_found:
                res.append(word_found)
        
            board[x][y] = '#'
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                _backtrack(nx, ny, current)
            board[x][y] = ch
            return

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    _backtrack(i, j, trie)
        return res
 