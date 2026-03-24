from typing import List, Optional

        
class Solution:
    def removePrefix(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            current = trie
            for ch in word:
                if ch not in current:
                    current[ch] = {}
                current = current[ch]
            current['#'] = True    
        res = []
        for word in words:
            current = trie
            for c in word:
                current = current[c]
            if len(current) == 1 and '#' in current:
                res.append(word)
        return res
                
'''
Time: O(N*L)
'''

