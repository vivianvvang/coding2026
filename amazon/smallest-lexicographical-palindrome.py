from typing import List, Optional
from collections import Counter
import heapq
class Solution:
    def findEncryptedPassword(self, s: str) -> str:
        counter = Counter(s)
        hq = []
        odd = 0
        for ch, count in counter.items():
            heapq.heappush(hq, (ch, count))
        left, mid = "", ""
        while hq:
            ch, count = heapq.heappop(hq)
            # if count % 2 == 0:
            #     left = left + ch * (count // 2)
            # else:
            #     if odd == 0:
            #         mid = ch
            #         heapq.heappush(hq, (ch, count - 1))
            #         odd += 1
            #     else:
            #         return ""
            if count % 2 == 1:
                odd += 1
                if odd > 1:
                     return ""
                mid = ch
            left += ch * (count // 2)
        return left + mid + left[::-1]


"""
Because the input contains only 26 lowercase letters, 
a heap is unnecessary. This is simpler:
    for ch in "abcdefghijklmnopqrstuvwxyz":
        count = counts[ch]
        ...
Counting takes (O(n)).
Iterating through 26 letters is (O(1)).
"""