from typing import List, Optional
import random

class Solution:
    def findMedian(self, nums: List[int]) -> float:
        
        def ksmall(left: int, right: int, k: int) -> int:
            while left <= right:
                pivot = random.randint(left, right)
                pivot_val = nums[pivot]
                # exchange right and pivot for convinience
                nums[right], nums[pivot] = nums[pivot], nums[right]
                cnt = left

                for i in range(left, right): #[left, right)
                    if nums[i] < pivot_val:
                        nums[cnt], nums[i] = nums[i], nums[cnt]
                        cnt += 1
                
                nums[right], nums[cnt] = nums[cnt], nums[right]

                if cnt == k:
                    return nums[cnt]
                elif cnt < k:
                    left = cnt + 1
                else:
                    right = cnt - 1
            return -1

        n = len(nums)
        if n % 2 == 1:
            return float(ksmall(0, n-1, n//2))
        else:
            left_mid = float(ksmall(0, n-1, n//2 -1))
            right_mid = float(ksmall(0, n-1, n//2))
            return (left_mid + right_mid) / 2.0


s = Solution()

print(s.findMedian([3, 1, 2, 4, 5]))

print(s.findMedian([7, 4, 1, 2]))

print(s.findMedian([9, 2, 5, 3, 5, 8, 9, 7, 9, 3, 2]))