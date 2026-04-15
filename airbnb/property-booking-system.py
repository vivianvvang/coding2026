from typing import List, Optional
from collections import defaultdict

#https://www.hack2hire.com/companies/airbnb/coding-questions/68b975288c4a0a9996afdd78/practice?questionId=68b975348c4a0a9996afdd79
class BookingSystem:
    def __init__(self, properties: List[List[str]]):
        self.neighbors = defaultdict(list)
        for id, n, cap in properties:
            self.neighbors[n].append((id, int(cap)))
        for neighborhood in self.neighbors:
            self.neighbors[neighborhood].sort(key=lambda x: x[0])
    
    def book(self, neighborhood: str, groupSize: int) -> List[str]:
        # TODO: Implement book logic
        properties = self.neighbors[neighborhood]
        memo = {} 
        #[key]: (pi, cap_to_book) 
        #[value]: （min total cap booked, list of properties booked）

        def dfs(idx, pending_cap):
            if pending_cap <= 0: 
                return (0, []) #need no more capacity or properties.
            if idx == len(properties):
                return (float('inf'), []) 
            if (idx, pending_cap) in memo:
                return memo[(idx, pending_cap)]
            id, cap = properties[idx]

            # choice 1: skip
            cap_booked_skip, properties_booked_skip = dfs(idx+1, pending_cap)
            # choice 2: take
            cap_booked_take_tmp, properties_booked_take = dfs(idx+1, pending_cap - cap)
            cap_booked_take = cap_booked_take_tmp + cap if cap_booked_take_tmp != float('inf') else float('inf')

            # goal 0: cap_booked != 'inf'
            # goal 1. min total cap booked
            # goal 2: min len(properties_booked)

            min_cap = float('inf')
            min_properties = []

            if cap_booked_skip < cap_booked_take:
                min_cap = cap_booked_skip
                min_properties = properties_booked_skip
            elif cap_booked_skip > cap_booked_take:
                min_cap = cap_booked_take
                min_properties = [id] + properties_booked_take
            else:
                min_cap = cap_booked_skip
                if min_cap != float('inf'):
                    # if tie on both, prefer take than skip (so prioritize getting the houses that are listed earlier)
                    min_properties = ([id] + properties_booked_take) if (len(properties_booked_take) + 1) <= len(properties_booked_skip) else properties_booked_skip

            memo[(idx, pending_cap)] = min_cap, min_properties
            return memo[(idx, pending_cap)]
        final_cap, final_properties = dfs(0, groupSize)
        return final_properties if final_cap != float('inf') else []
    
'''
N: number of properties, C: groupSize
Time Complexity: O(N * C)
Space: O(N * C)
'''