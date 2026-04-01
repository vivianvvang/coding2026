#
# @lc app=leetcode id=1055 lang=python3
#
# [1055] Shortest Way to Form String
#

# @lc code=start
class Solution:
    # Time Complexity: $O(S*T)
    def shortestWay(self, source: str, target: str) -> int:
        source_chars = set(source)
        for char in target:
            if char not in source_chars:
                return -1
        count = 0 # num of seqs needed
        pt = 0 # pointer of target
        while pt < len(target):
            count += 1
            for s in source:
                if pt < len(target) and s == target[pt]:
                    pt += 1
        return count
# @lc code=end

