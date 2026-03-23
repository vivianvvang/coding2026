from typing import List, Optional
from collections import defaultdict
class Solution:
    def findMaxScorePath(self, routes: List[List[str]], checkpoints: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        rewards = defaultdict(int)
        for point, cost, to in routes:
            graph[point].append((to, int(cost)))
        for checkpoint, reward in checkpoints:
            rewards[checkpoint] = int(reward)

        memo = {}
        
        def dfs(node): # return (score, path)
            if node.startswith("END_"):
                return (rewards[node], [node])
            if node in memo:
                return memo[node]
            
            max_score = -float('inf')
            max_path = []
            
            for neighbor, cost in graph[node]:
                n_score, n_path = dfs(neighbor)
                tmp_score, tmp_path = rewards[node] + n_score - cost, [node] + n_path
                if tmp_score > max_score:
                    max_score = tmp_score
                    max_path = tmp_path
                
            memo[node] = (max_score, max_path)
            
            return memo[node]

        _, res_path = dfs("START")
        return res_path

'''
Time Complexity: O(V + E)
'''

