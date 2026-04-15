from typing import List, Optional
from collections import defaultdict
# https://www.hack2hire.com/companies/airbnb/coding-questions/68baf382b5314dcd938cba01/practice?questionId=68baf390b5314dcd938cba02 

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
        prefix = defaultdict(list) #x -> listing that is available from [start, x]
        suffix = defaultdict(list) #y -> listing that is available from [y, end]
        res = set()

        for i, listing in enumerate(listings): # N
            for p in range(start, end): # D
                if p in listing: 
                    prefix[p].append(i)
                else:
                    break
            for s in range(end, start, -1):
                if s in listing:
                    suffix[s].append(i)
                else:
                    break
        
        for day in range(start, end):
            first, sec = prefix[day], suffix[day + 1]
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