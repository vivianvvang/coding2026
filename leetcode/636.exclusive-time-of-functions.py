#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        prev_start = 0
        call_stack = []
        for log in logs:
            strs = log.split(":")
            idx, status, time = int(strs[0]), strs[1], int(strs[2])
            if status == "start":
                if call_stack:
                    res[call_stack[-1]] += (time - prev_start)
                prev_start = time

                call_stack.append(idx)

            else:
                call_stack.pop()
                res[idx] += (time - prev_start + 1)
                prev_start = time + 1
        return res
        
# @lc code=end

