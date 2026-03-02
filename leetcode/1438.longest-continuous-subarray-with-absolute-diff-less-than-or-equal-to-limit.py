#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
from collections import deque
from typing import List
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()
        l = 0
        ans = 0
        for i, num in enumerate(nums):
            while min_q and num < min_q[-1]:
                # to keep min_q from small to large
                min_q.pop()
            min_q.append(num)
            while max_q and num > max_q[-1]:
                max_q.pop()
            max_q.append(num)
            
            while len(max_q) > 0 and len(min_q) > 0 and max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[l]:
                    max_q.popleft()
                if min_q[0] == nums[l]:
                    min_q.popleft()
                l += 1
            ans = max(ans, i - l + 1)
        return ans 
# @lc code=end

