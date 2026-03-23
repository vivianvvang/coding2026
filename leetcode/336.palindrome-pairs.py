#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
# Case 1: Reverse whole word and concat to form
# Case 2: Current word prefix reversed is another word, remaing word itself is palindrome
# Case 2L Current word suffix reversed is another word, reamining word is palindrome
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def all_valid_prefixes(word):
            prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    prefixes.append(word[:i])
            return prefixes


        def all_valid_suffixes(word):
            suffixes = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    suffixes.append(word[i+1:])
            return suffixes

        word_lookup = {word: i for i, word in enumerate(words)}

        res = []

        for idx, word in enumerate(words):
            reversed_word = word[::-1]

            if reversed_word in word_lookup and word_lookup[reversed_word] != idx:
                res.append([idx, word_lookup[reversed_word]])

            for prefixes in all_valid_prefixes(word):
                reversed_prefixes = prefixes[::-1]
                if reversed_prefixes in word_lookup and word_lookup[reversed_prefixes] != idx:
                    res.append([idx, word_lookup[reversed_prefixes]])

            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup and word_lookup[reversed_suffix] != idx:
                    res.append([word_lookup[reversed_suffix], idx])

        return res




# @lc code=end

