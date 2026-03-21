from typing import List

class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self, word: str, category: str) -> None:
        current = self.trie
        for ch in word:
            if ch not in current:
                current[ch] = {}
            current = current[ch]
        current['#'] = category
    

class Solution:
    def highlightPhrases(self, review: str, mapping: List[List[str]]) -> str:
        ps, pe = 0, 0 # pointer start and end
        trie = Trie()
        for phrase, catagory in mapping:
            trie.insert(phrase.lower(), catagory)
        res = []
        while ps < len(review):
            pe = ps
            curr = trie.trie
            longest_valid_e, cat = ps, None
            while pe < len(review) and (review[pe].isalnum() or review[pe] == " ") and review[pe].lower() in curr:
                curr = curr[review[pe].lower()]
                if '#' in curr:
                    longest_valid_e, cat = pe, curr['#']
                pe += 1
            if cat:
                res.append(f"[{cat}]{{{review[ps:longest_valid_e+1]}}}")
                ps, pe = longest_valid_e + 1, longest_valid_e + 1
            else:
                res.append(review[ps])
                ps, pe = ps + 1, ps + 1

        return "".join(res)
                

# O((M + N) × L), N is the length of the review string, 
# M is the number of phrases in the mapping, 
# L is the average length of a phrase in the mapping.