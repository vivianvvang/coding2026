#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#
from typing import List
# @lc code=start
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set([(x, y) for x, y in points])
        res = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if y1 == y2 or x1 == x2:
                    continue
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    res = min(res, abs(x1 - x2) * abs (y1 - y2))
        return res if res < float('inf') else 0
        
        
        
# @lc code=end

