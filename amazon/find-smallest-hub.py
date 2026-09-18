from typing import List, Optional

class Solution:
    def findSmallestHub(self, capacities: List[int], intervals: List[List[str]], requiredCapacity: int, taskInterval: str) -> int:
        ans = -1
        best_cap = float('inf')
        taskIntervals = taskInterval.split(":")
        ts, te = int(taskIntervals[0]), int(taskIntervals[1])
        n = len(capacities)

        for i in range(n):
            cap = capacities[i]
            if cap < requiredCapacity:
                continue
            
            conflict = False
            for interval in intervals[i]:
                parts = interval.split(":")
                start, end = int(parts[0]), int(parts[1])
                if not (start >= te or end <= ts):
                    conflict = True
                    break
            if conflict:
                continue

            if cap < best_cap:
                ans = i
                best_cap = cap

        return ans
            

