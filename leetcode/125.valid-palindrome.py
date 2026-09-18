#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(filter(str.isalnum, s)).lower()
        reversed_s = filtered_s[::-1]
        return filtered_s == reversed_s
# @lc code=end

