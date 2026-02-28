from typing import List, Optional

class Solution:
    def nextPalindrome(self, n: str) -> str:
        len_n = len(n)
        i = len_n // 2 -1 if len_n % 2 == 0 else len_n // 2
        first_half = int (n[0: i + 1])

        possibilities = []

        # 1. Create a palindrome by mirroring the first half.
        # eg: 4567 -> 4554
        possibilities.append(self.half_to_palindrome(first_half, len_n % 2 == 0))

        # 2. Create a palindrome by mirroring the first half incremented by 1.
        # eg: 123 -> 12 + 1 -> 131
        possibilities.append(self.half_to_palindrome(first_half + 1, len_n % 2 == 0))

        # 3. Handle edge cases by considering palindromes of the form 999... 
        #    and 100...001 (smallest and largest n-digit palindromes).
        # possibilities.append(10 ** (len_n -1) - 1)
        # if n conisists 9 only, next palindrome is 10xxx01
        possibilities.append(10 ** len_n + 1)

        res = float("inf")
        origin = int(n)

        for cand in possibilities:
            if cand <= origin:
                continue
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