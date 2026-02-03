#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
# two pointers.
from typing import List

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        max_left, max_right = height[0], height[-1]
        pl, pr = 0, len(height) - 1
        while pl < pr:
            res = max(res, min(max_left, max_right) * (pr - pl))
            if max_left <= max_right:
                while pl < pr and max_left >= height[pl]:
                    pl += 1
                max_left = max(max_left, height[pl])
            else: 
                while pl < pr and max_right >= height[pr]:
                    pr -= 1
                max_right = max(max_right, height[pr])

        return res
# @lc code=end