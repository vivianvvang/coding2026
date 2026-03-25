from typing import List, Optional

class Solution:
    def generateEmailBody(self, detectedWords: List[str], categories: List[List[str]], instructions: List[List[str]]) -> List[List[str]]:
        category = {}
        instruction = {}
        for cat in categories:
            category[cat[0]] = cat[1]
        for inst in instructions:
            instruction[inst[0]] = inst[1].strip()
        
        categoryOrder = []
        keywords = {}
        ans = []

        for word in detectedWords:
            c = category.get(word)
            if c is not None:
                if c not in keywords:
                    categoryOrder.append(c)
                    keywords[c] = set()
                keywords[c].add(word)
        
        res = []
        for c in categoryOrder:
            res = []
            sorted_words = list(keywords[c])
            sorted_words.sort()
            detected_words_str =  ", ".join(sorted_words)
            res.append("Detected Keywords: " + detected_words_str)

            # instructions:
            instruction_str = "Instruction: " + instruction[c]
            res.append(instruction_str)
            
            ans.append(res)
        return ans
            