#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtracking(i, target, result):
            if target <= 0:
                if target == 0:
                    ans.append(result[:])
                return
            if i >= len(candidates):
                return

            for j in range(i, len(candidates)):
                result.append(candidates[j])
                backtracking(j, target - candidates[j], result)
                result.pop()
            return
        backtracking(0, target, [])
        return ans
# @lc code=end

