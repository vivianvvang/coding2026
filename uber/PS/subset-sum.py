from typing import List, Optional

class Solution:
    def subsetSum(self, nums: List[int], target: int) -> bool:
        dp = [False] * (target + 1)
        dp[0] = True
        # dp[i] = dp[i]  or  dp[i - num]

        for num in nums:
            # 从后往前遍历，确保每个数字只用一次
            # 范围是 [target, num]，步长为 -1
            print(" -------------- ", num, "---------------")
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
            # 提前剪枝：如果已经凑出了 target，直接返回 True
            print(dp)
            if dp[target]:
                return True
                
        return dp[target]
solution = Solution()

print(solution.subsetSum([2, 5, 3, 11], 10)) # True (2+5+3)
# print(solution.subsetSum([3, 9, 4], 8))       # False
# print(solution.subsetSum([1, 2, 3, 7], 6))    # True (1+2+3)