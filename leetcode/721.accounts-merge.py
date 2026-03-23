#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        graph = defaultdict(list)
        for account in accounts:
            name = account[0]
            len_a = len(account)
            for i in range(1, len_a):
                for j in range(i, len_a):
                    graph[(account[i], name)].append((account[j], name))
                    graph[(account[j], name)].append((account[i], name))
        
        visited = set()
        def dfs(email, name, res):
            visited.add(email)
            res.add(email)
            for next_email, _ in graph[(email, name)]:
                if next_email not in visited:
                    dfs(next_email, name, res)
        
        ans = []
        for email, name in graph.keys():
            res = set()
            if email not in visited:
                dfs(email, name, res)
                ans.append([name] + sorted(list(res)))
        
        return ans

# @lc code=end
'''
N: number of accounts
K: maximum len of an account.
Time complexity: O(NKlogNK)
'''
