from typing import List, Optional

class Solution:
    def wrapSubstrings(self, s: str, elements: List[str]) -> str:
        elementSet = set(elements)
        words = s.split()
        result = []
        for word in words:
            matched = False
            for i in range(len(word)): # 0 -> N-1
                for j in range(i + 1, len(word) + 1): # i+1 -> N, on average: N/2
                    # O(N * (N - 1) / 2) = O(N^2)
                    substr = word[i:j]
                    print(substr)
                    if substr in elementSet:
                        result.append(word[:i] + "[" + substr + "]" + word[j:])
                        matched = True
                        break
                if matched:
                    break
            if not matched:
                result.append(word)
        return " ".join(result)