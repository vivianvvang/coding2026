from typing import List, Optional

class Solution:
    def wrapSubstrings(self, s: str, elements: List[str]) -> str:
        substrings = s.split()
        ans = [" "] * len(substrings)
        for ele in elements:
            for i, s in enumerate(substrings):
                if '[' not in ans[i]:
                    index = s.find(ele)
                    if index != -1:
                        ts = s[0: index] + '[' + ele + ']' + s[index + len(ele): len(s)]
                        ans[i] = ts
        for i, s in enumerate(substrings):
            if ans[i] == " ":
                ans[i] = s
        return " ".join(ans)
