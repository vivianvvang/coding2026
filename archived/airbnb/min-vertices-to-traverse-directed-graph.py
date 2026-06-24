from typing import List, Optional
from collections import deque

class Solution:
    def minStartPoints(self, n: int, edges: List[List[int]]) -> int:
        # Kosaraju Algorithm: find SCC with original and reverse graph
        graph = [[] for _ in range(n)] # n empty lists
        reverseGraph = [[] for _ in range(n)]
        for start, end in edges:
            graph[start].append(end)
            reverseGraph[end].append(start)
        
        # Step 1: traverse original graph with DFS 
        # push nodes to stack with their finish order
        visited = [False] * n
        stack = [] # stack

        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)
        
        for i in range(n):
            if visited[i] != True:
                dfs(i)
        
        # Step 2: Label nodes in same SCC
        scc_map = [-1] * n # strong connected component
        visited_reverse = [False] * n
        scc_count = 0

        def dfsLableScc(node, scc_id):
            visited_reverse[node] = True
            scc_map[node] = scc_id #nodes in scc will have same scc_id
            
            for neighbor in reverseGraph[node]:
                if not visited_reverse[neighbor]:
                    dfsLableScc(neighbor, scc_id)
        
        while stack:
            node = stack.pop()
            if not visited_reverse[node]:
                dfsLableScc(node, scc_count)
                scc_count += 1

        # Step 3: Calculate indegree based on condensed DAG
        if scc_count == 1:
            return 1

        indegree = [0] * scc_count
        for node in range(n):
            for neighbor in graph[node]:
                if scc_map[node] != scc_map[neighbor]: # not in a circle
                    indegree[scc_map[neighbor]] += 1
        return sum(1 for degree in indegree if degree == 0)
    
# Time Complexity: O(V + E), V = number of nodes, E = number of edges
# Space Complexity: Same 

s = Solution()
print(s.minStartPoints(5, [[0, 1], [1, 2], [2, 0], [3, 4]])) #2
print(s.minStartPoints(6, [[0, 1], [1, 0], [2, 1], [2, 5], [5, 4], [1, 3]])) #1
print(s.minStartPoints(6, [[0, 1], [1, 0], [2, 1], [1, 3], [5, 4]])) #2
                    


