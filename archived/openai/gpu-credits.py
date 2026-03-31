from typing import List, Optional
from collections import defaultdict
import heapq

# events may come out of order, do lazy evalution: calculate on getBalence
class CreditSystem:
    def __init__(self, ):
        self.grants = defaultdict(list) #startTime -> (exp, amount)
        self.subtractions = defaultdict(int) # timestamp -> amount

    def grantCredit(self, id: str, amount: int, startTime: int, expirationTime: int) -> None:
        self.grants[startTime].append((expirationTime, amount))
    
    def subtract(self, amount: int, timestamp: int) -> None:
        self.subtractions[timestamp] += amount
            
    def getBalance(self, timestamp: int) -> int:
        pq = []
        ts = set() # all ts <= given timestamp
        for t in self.grants.keys():
            if t <= timestamp:
                ts.add(t)
        for t in self.subtractions.keys():
            if t <= timestamp:
                ts.add(t)
        for t in sorted(ts):
            # remove invalid ???
            while pq and pq[0][0] <= t:
                heapq.heappop(pq)
            for exp, amount in self.grants[t]:
                heapq.heappush(pq, (exp, amount))
            
            consumed = self.subtractions[t]
            while consumed > 0 and pq:
                exp, amount = heapq.heappop(pq) # earliest expiring grant
                curr_cost = min(consumed, amount)
                consumed -= curr_cost
                
                if amount > 0: #current grant still has grant, push back to pq
                    heapq.heappush(pq, (exp, amount - curr_cost))
                

        # remove expiring grants
        while pq and pq[0][0] <= timestamp:
            heapq.heappop(pq)
        return sum(amount for _, amount in pq)
