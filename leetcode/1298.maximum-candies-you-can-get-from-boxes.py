#
# @lc app=leetcode id=1298 lang=python3
#
# [1298] Maximum Candies You Can Get from Boxes
#

# @lc code=start
from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        visited = set()
        to_open = set()
        q = deque()
        res = 0 

        for b in initialBoxes:
            if status[b] == 1:
                q.append(b)
            else:
                to_open.add(b)
        
        while len(q) > 0:
            box = q.popleft()
            visited.add(box)
            res += candies[box]
            
            # get keys
            for key in keys[box]:
                status[key] = 1
                if key in to_open and key not in visited:
                    q.append(key)
                    to_open.remove(key)
            # get contained boxes
            for cbox in containedBoxes[box]:
                if cbox not in visited:
                    if status[cbox] == 1:
                        q.append(cbox)
                    else:
                        to_open.add(cbox)
            
        return res

# Time: O(N^2), Space: O(N)
# @lc code=end

