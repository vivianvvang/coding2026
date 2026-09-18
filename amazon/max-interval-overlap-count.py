from typing import List

class Solution:
    def maxOverlap(self, intervals: List[List[int]]) -> int:
        starts = sorted(interval[0] for interval in intervals)
        ends = sorted(interval[1] for interval in intervals)
        n = len(intervals)
        curr = 0
        ans = 0
        i, j = 0, 0
        while i < n:
            if starts[i] <= ends[j]:
                curr += 1
                ans = max(curr, ans)
                i += 1
            else:
                curr -= 1
                j += 1
        return ans


