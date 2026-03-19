from typing import List, Optional
from collections import defaultdict

class Solution:
    def splitStayCombinations(self, listings: List[List[int]], start: int, end: int) -> List[List[int]]:
        n = len(listings)
        listing_sets = [set(days) for days in listings] # O(N * L)

        # Phase 1: single stays
        single_stays = []
        full_stay = set(range(start, end + 1))
        
        for i in range(n):
            if full_stay.issubset(listing_sets[i]):
                single_stays.append([i])
        if single_stays:
            return single_stays
        
        # Phase 2: split stays
        prefix = defaultdict(list)
        suffix = defaultdict(list)
        res = set()

        for i, l in enumerate(listings): # N
            for k in range(start, end): # D
                # if set(range(start, k+1)).issubset(l): # create set: D 
                #     prefix[k].append(i)
                # if set(range(k, end)).issubset(l):
                #     suffix[k].append(i)
                if k in l: 
                    prefix[k].append(i)
                else:
                    break
            for m in range(end, start, -1):
                if m in l:
                    suffix[m].append(i)
                else:
                    break
        
        for k in range(start, end):
            first, sec = prefix[k], suffix[k+1]
            for i in first:
                for j in sec:
                    if i != j:
                        res.add((i, j))
        return [list(stay) for stay in res]

'''
N: number of listings
D: duration
L: avg of available days per listing
updated solution: O(N*L + N*D + D*N^2)
subset solution: O(N*L + N*D^2 + D*N^2)
'''