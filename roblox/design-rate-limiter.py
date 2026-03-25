from typing import List, Optional
from collections import deque
class Solution:
    # def rateLimit(self, timestamps: List[int], maxRequests: int, windowSize: int) -> List[bool]:
    #     start_idx, num_requests, accepted_requests = 0, 0, 0
    #     res = []
    #     for ts in timestamps:
    #         while ts - timestamps[start_idx] >= windowSize:
    #             if res[start_idx] == True:
    #                 num_requests -= 1
    #             start_idx += 1
            
    #         if num_requests < maxRequests:
    #             num_requests += 1
    #             res.append(True)
    #         else:
    #             res.append(False)
    #     return res

    def rateLimiterQueue(self, timestamps, maxRequests, windowSize):
        res = []
        q = deque()

        for _, ts in enumerate(timestamps):
            windowStart = ts - windowSize + 1
            while len(q) > 0 and q[0] < windowStart:
                q.popleft()
            if len(q) < maxRequests:
                q.append(ts)
                res.append(True)
            else:
                res.append(False)
s = Solution()
s.rateLimit([1, 2, 3, 6], 2, 5)
