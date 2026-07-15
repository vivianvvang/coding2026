from typing import List, Optional
import re
from collections import Counter
import heapq


class Solution:
    def top10FrequentWords(self, s: str) -> List[List[str]]:
        words = re.findall(r'[a-zA-Z]+', s)
        words = [word.lower() for word in words]

        word_count = Counter(words)

        # Order from largest frequency, if tie, ascending lexi order
        # Pick top 10, so we use nsmallest, negative the count
        topk = heapq.nsmallest(10, word_count.items(), key=lambda kv: (-kv[1], kv[0]))

        return [[w, str(c)] for w, c in topk]
    


# Follow up OOD

import re
from collections import Counter
from typing import List, Optional
import heapq

# You should NOT access to the text directly, all data can only be access from `getNextBatch`
class ExternalBatchAPI:
    def __init__(self, text: str):
        self.text = text
        self.position = 0

    def getNextBatch(self, batchSize) -> Optional[str]:
        if self.position >= len(self.text):
            return None

        batch = self.text[self.position:self.position + batchSize]
        self.position += len(batch)
        return batch

class Top10Words:
    def __init__(self, text: str, batchSize: int):
        self.api = ExternalBatchAPI(text)
        self.batchSize = batchSize
        self.wordCounts = Counter()
        self.leftover = ""

    def processAllText(self) -> List[List[str]]:
        while True:
            batch = self.api.getNextBatch(self.batchSize)
            if not batch:
                break
            self.processBatch(batch)

        if self.leftover:
            word = self.extractWords(self.leftover)
            self.wordCounts.update(word)
        return self.getTop10()
    
    def processBatch(self, batch):
        text = self.leftover + batch
        
        lastSpace = text.rfind(' ')
        if lastSpace == -1:
            # No space found - entire text might be one word or fragment
            self.leftover = text
        else:
            completeText = text[:lastSpace]
            self.leftover = text[lastSpace + 1:]

            words = self.extractWords(completeText)
            self.wordCounts.update(words)

    def extractWords(self, text: str) -> List[str]:
        words = re.findall(r'[a-zA-Z]+', text)
        return [word.lower() for word in words]

    def getTop10(self) -> List[List[str]]:
        if not self.wordCounts:
            return []

        # Use nsmallest with a key to get top 10: sort by count desc, then word asc
        topk = heapq.nsmallest(10, self.wordCounts.items(), key=lambda kv: (-kv[1], kv[0]))

        return [[w, str(c)] for w, c in topk]

if __name__ == "__main__":
    print("========== Example 1 ==========")
    text1 = "The quick brown fox jumps over the lazy dog. The dog was really lazy."
    print("text:", f"'{text1}', batchSize: 20")    # text length: 64
    processor = Top10Words(text1, 20)
    result1 = processor.processAllText()
    # Expected: [['the', '3'], ['dog', '2'], ['lazy', '2'], ['brown', '1'], ['fox', '1'], ['jumps', '1'], ['over', '1'], ['quick', '1'], ['really', '1'], ['was', '1']]
    print("Result:", result1)
    print('\n')


    print("========== Example 2 ==========")
    text2 = "apple banana cherry " * 100 + "apple " * 50
    print("text:", f"'apple banana cherry ' * 100 + 'apple ' * 50, batchSize: 100")    # text length: 2300
    processor = Top10Words(text2, 100)
    result2 = processor.processAllText()
    # Expected: [['apple', '150'], ['banana', '100'], ['cherry', '100']]
    print("Result:", result2[:3])
    print('\n')


    print("========== Example 3 ==========")
    text3 = "hello world test hello programming"
    print("text:", f"'{text3}', batchSize: 10")    # text length: 42
    processor = Top10Words(text3, 10)
    result3 = processor.processAllText()
    # Expected: [['hello', '2'], ['programming', '1'], ['test', '1'], ['world', '1']]
    print("Result:", result3)
    print('\n')


    print("========== Example 4 ==========")
    text4 = ""
    print("text:", f"'{text4}', batchSize: 100")    # text length: 0
    processor = Top10Words(text4, 100)
    result4 = processor.processAllText()
    # Expected: []
    print("Result:", result4)
    print('\n')

    print("========== Example 5 ==========")
    text5 = "word " * 50
    print("text:", f"'word ' * 50, batchSize: 20")    # text length: 100
    processor = Top10Words(text5, 20)
    result5 = processor.processAllText()
    # Expected: [['word', '50']]
    print("Result:", result5)
    print('\n')
        



        
