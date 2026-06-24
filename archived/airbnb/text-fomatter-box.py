from typing import List, Optional

class Solution:
    def formatBox(self, sentences: List[str]) -> List[str]:

        max_len = -1
        for sentence in sentences:
            max_len = max(max_len, len(sentence))
        
        boarder = "+" + "-" * max_len + "+"
        fb = []
        for s in sentences:
            fb.append(boarder)
            fb.append("|" + s + " " * (max_len - len(s)) + "|")
        fb.append(boarder)
        return fb