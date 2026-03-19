#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        def cal_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 - x2 == 0:
                return float("inf")
            return (y1 - y2) / (x1 - x2)

        ans = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for j, p2 in enumerate(points[i+1: ]):
                slope = cal_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans + 1



        
# @lc code=end

