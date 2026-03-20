#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#
# @lc code=start
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))

        memo = {}
        # memo[i]: starting from job i, max profit can earn
        
        def find_next(idx, lastEnd):
            # while idx < n:
            #     if jobs[idx][0] >= lastEnd:
            #         return idx
            #     idx += 1
            # return -1
            l, r = idx, n
            while l < r:
                mid = l + (r - l) // 2
                if jobs[mid][0] >= lastEnd:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        def dfs(id):
            if id == n:
                return 0
            if id in memo:
                return memo[id]
            next_idx = find_next(id + 1, jobs[id][1])
            p_take = jobs[id][2]
            if next_idx >= 0:
                p_take += dfs(next_idx)
            memo[id] = max(dfs(id + 1), p_take)
            return memo[id]
        
        return dfs(0)

# @lc code=end

'''
Time: O(NlogN) binarySearch + scan
Space: O(N)  stack size: N. storage: 3N
'''