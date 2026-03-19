from typing import List, Optional

class Solution:
    def minCostToOrder(self, menu: List[List[str]], userWants: List[str]) -> List[List[str]]:
        initial_wants = tuple(sorted(userWants))
        
        # pre-processing
        processed_menu = []
        for id, price_str, items in menu:
            price = round(float(price_str) * 100)
            item_list = items.split(",")
            item_provided = set(userWants) & set(item_list)
            if len(item_provided) > 0:
                processed_menu.append((id, price, tuple(sorted(item_provided))))
            
        memo = {}

        def dfs(idx, pending):
            if len(pending) == 0:
                return (0, [[]]) # one availble path with no entry to take
            if idx == len(processed_menu):
                return (float('inf'), [])
            # check cache
            if (idx, pending) in memo:
                return memo[(idx, pending)]
            
            entry_id, price, items = processed_menu[idx]

            # choice 1: skip this enty
            cost_skip, paths_skip = dfs(idx+1, pending)
            # choice 2: take this entry
            cost_take_tmp, paths_take_tmp = dfs(idx+1, tuple(sorted(set(pending) - set(items))))
            cost_take = cost_take_tmp + price

            min_cost = float('inf')
            min_paths = []

            if cost_skip < cost_take:
                min_cost = cost_skip
                min_paths = paths_skip
            elif cost_skip > cost_take:
                min_cost = cost_take
                min_paths = [[entry_id] + path for path in paths_take_tmp] 
            else:
                min_cost = cost_skip
                if min_cost != float('inf'):
                    min_paths = paths_skip + [[entry_id] + path for path in paths_take_tmp]
            
            # add to cache
            memo[(idx, pending)] = (min_cost, min_paths)
            return memo[(idx, pending)]

        final_cost, final_paths = dfs(0, initial_wants)

        return final_paths if final_cost != float('inf') else []

'''
N: number of menus
W: number of userWants items
Time: 
- Cache key (the "State") is (idx, pendings).
- Pendings is a subset of userWants, W items -> 2 * W posiible subsets
- States X Work per State = O(N * 2^W * W)
Space: O(N * W * 2^W)
'''