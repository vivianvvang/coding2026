#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#

# @lc code=start
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n

        visited = set()
        for src, dst in edges:
            visited.add(dst)
            indegree[dst] += 1

        res = []
        for i in range(n):
            if indegree[i] == 0:
                res.append(i)

        return res        
# @lc code=end

