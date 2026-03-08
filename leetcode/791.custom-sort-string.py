#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        ans = ""
        for ch in order:
            if ch in counter:
               ans += ch * counter[ch]
               del counter[ch]
        for ch, times in counter.items():
            ans += ch * times
        return ans
        
# @lc code=end

