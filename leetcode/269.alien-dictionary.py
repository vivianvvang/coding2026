#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
from typing import List
from collections import defaultdict, deque
# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # build adj list
        def sortByCharacter(a, b): 
            for i in range(min(len(a), len(b))):
                if a[i] != b[i]:
                    return (a[i], b[i])
            if len(a) > len(b):
                return ('*', '*')
            else:
                return('-', '-')
        
        indegree = { c: 0 for word in words for c in word }
        adj = defaultdict(set)

        # build adj list
        for i in range(len(words) - 1):
            a, b = sortByCharacter(words[i], words[i+1])
            if a == '*':
                return ""
            elif a == '-':
                continue
            else:
                if b not in adj[a]:
                    indegree[b] += 1
                    adj[a].add(b)
                

        q = deque()
        ans = ""
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
        
        while q:
            node = q.popleft()
            ans += node
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        # for k, v in indegree.items():
        #     if v != 0:
        #         return ""
        if len(ans) < len(indegree.keys()):
            return ""
        return ans
        
        
# @lc code=end

