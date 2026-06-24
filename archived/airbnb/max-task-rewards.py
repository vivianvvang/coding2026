from typing import List, Optional
import heapq

class Solution:
    def maximumRewards(self, tasks: List[List[str]]) -> List[str]:
        processed_tasks = []

        '''
        Greedy, Sort all tasks in descending order of profit
        For each task in sorted order, try to assign it to the 
        latest free slot from its deadline
        '''
        for task in tasks:
            name, ddl, p = task[0], int(task[1]), int(task[2])
            processed_tasks.append((name, ddl, p))
        processed_tasks.sort(key = lambda x:(x[1], -x[2])) # sort by ddl asc, profit dsc

        hq = [] # min heap based on profit

        for name, ddl, p in processed_tasks:
            heapq.heappush(hq, (p, ddl, name))

            if len(hq) > ddl:
                # remove least profitable task if needed
                heapq.heappop(hq)
        # now hq contains the optimal subset of tasks
        # sort again by ddl
        schedule = sorted(hq, key = lambda x: x[1])
        return [task[2] for task in schedule]
    
        '''
        Time: N * Log(N)
        Space: N
        '''