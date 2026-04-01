#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    """
    We perform a DFS. When a node has no more outgoing edges to explore, 
    we add it to our result. Because we do this as we "backtrack," 
    the result will be in reverse order.
    Time Complexity: O(NlogN)
    """

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        
        # 2. sort reversely, so it can be pop first using pop()
        for src in adj:
            adj[src].sort(reverse=True)

        res = []
        def dfs(curr):
            # 3. 只要当前机场还有票，就飞往列表末尾的那个机场 (pop 是 O(1))
            while adj[curr]:
                next_dest = adj[curr].pop()
                dfs(next_dest)
            
            # 4. 走投无路时，说明它是当前的终点，加入结果
            res.append(curr)
        dfs("JFK")
        # 5. 因为是回溯时记录的，所以结果是反的，需要反转回来
        return res[::-1]
# @lc code=end

