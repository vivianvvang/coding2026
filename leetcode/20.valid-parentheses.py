#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i, char in enumerate(s):
            if char in ('(', '{', '['):
                stk.append(char)
            else:
                if len(stk) == 0:
                    return False
                if (stk[-1] == '(' and char == ')') or (stk[-1] == '{' and char == '}') or (stk[-1] == '[' and char == ']'):
                    stk.pop()       
                else: return False      
        return len(stk) == 0
# @lc code=end

