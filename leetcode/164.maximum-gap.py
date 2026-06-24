#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
from typing import List
# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        min_v, max_v = min(nums), max(nums)
        if min_v == max_v:
            return 0

        b_size = max(1, (max_v - min_v) // (n - 1))
        b_count = (max_v - min_v) // b_size + 1
        buckets = [[float("inf"), float("-inf")] for _ in range(b_count)]
                   
        for num in nums:
            idx = (num - min_v) // b_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        res = 0
        prev_max = min_v
        for b_min, b_max in buckets:
            if b_min == float("inf"):
                continue
            res = max(res, b_min - prev_max)
            prev_max = b_max
        return res
# @lc code=end

