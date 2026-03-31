#
# @lc app=leetcode id=564 lang=python3
#
# [564] Find the Closest Palindrome
#

# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        len_n = len(n)
        i = len_n // 2 - 1 if len_n % 2 == 0 else len_n // 2
        first_half = int (n[0: i + 1])
        
        # Generate possible palindromic candidates:
        possibilities = []

        # 1. Create a palindrome by mirroring the first half.
        possibilities.append(self.half_to_palindrome(first_half, len_n % 2 == 0))

        # 2. Create a palindrome by mirroring the first half incremented by 1.
        possibilities.append(self.half_to_palindrome(first_half + 1, len_n % 2 == 0))

        # 3. Create a palindrome by mirroring the first half decremented by 1.
        possibilities.append(self.half_to_palindrome(first_half - 1, len_n % 2 == 0))

        # 4. Handle edge cases by considering palindromes of the form 999... 
        #    and 100...001 (smallest and largest n-digit palindromes).
        possibilities.append(10 ** (len_n -1) - 1)
        possibilities.append(10 ** len_n + 1)

        res = 0
        origin = int(n)
        diff = float("inf")

        for cand in possibilities:
            if cand == origin:
                continue
            if abs(cand - origin) < diff:
                diff = abs(cand - origin)
                res = cand
            elif abs(cand - origin) == diff:
                res = min(res, cand)
        return str(res)

    
    def half_to_palindrome(self, left: int, even: bool) -> int:
        res = left
        if not even:
            left = left // 10
        while left > 0:
            res = left % 10 + res * 10
            left //= 10
        return res

# @lc code=end

