from typing import List, Optional

class Solution:
    def findOriginals(self, encoded: str) -> List[str]:
        res = []
        if encoded is None or len(encoded) < 2:
            return res
        
        def backtrack(s, index, curr, res):
            if index == len(s):
                res.append(''.join(curr))
                return
            # At each call, try a count length of 1 or 2 characters.
            for l in range(1, 3):
                if index + l >= len(s):
                    break
                text = s[index:index + l]
                if text.startswith("0"):
                    continue
                count = int(text)
                if count < 1:
                    continue
                
                digit = s[index + l]
                prev_len = len(curr)
                curr.extend([digit] * count)

                backtrack(s, index + l + 1, curr, res)
                
                del curr[prev_len: ]
        
        backtrack(encoded, 0, [], res)
        return res
    
# Time Complexity: O(two to the N over two, times N)