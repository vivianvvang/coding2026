from typing import List, Optional
from collections import defaultdict
class Solution:
    def findMostFrequentCallStack(self, traces: List[str]) -> List[str]:
        stack = []
        freq = defaultdict(int)

        for trace in traces:
            if trace.startswith("-> "):
                funcName = trace[3:]
                stack.append(funcName)

                curr_state = " -> ".join(stack)
                freq[curr_state] += 1
            elif trace.startswith("<- "):
                stack.pop()
            
        res, max_freq, max_depth = "", 0, 0
        for state, count in freq.items():
            d = len(state.split(" -> "))
            if count > max_freq or (count == max_freq and d > max_depth):
                res, max_freq, max_depth = state, count, d
        return [res, str(max_freq)]

s = Solution()
res = s.findMostFrequentCallStack(["-> main","-> onButtonPress","-> validateUserInput","<- validateUserInput","-> validateUserInput","<- validateUserInput","<- onButtonPress","-> onKeyboardInput","<- onKeyboardInput","<- main"])
print(res)