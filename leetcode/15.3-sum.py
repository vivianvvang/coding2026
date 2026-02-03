#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums = [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        res = []
        d = dict()
        n = len(nums)

        for i in range(n):
            if nums[i] > 0: 
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res
# @lc code=end

