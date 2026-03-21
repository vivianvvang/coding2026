from typing import List, Optional
from collections import defaultdict
class Solution:
    def allocateRefunds(self, transactions: List[List[str]], refundAmount: int) -> List[List[str]]:
        
        self.trans = [] # list of transactions (payment_id, payment type, recency, amount), sort by payment, recency
        self.map = defaultdict(int) # payment_id -> list of refunds amount
        self.refundAmount = refundAmount

        for id, action, payment_type, linked_paymemt_id, ts, amount in transactions:
            if action == "PAYMENT":
                date_int = int(ts.replace("-", ""))
                self.trans.append((id, payment_type, date_int, int(amount)))
            else:
                self.map[linked_paymemt_id] += int(amount)
        self.trans = sorted(self.trans, key=lambda x: (x[1], -x[2]))

        res = []
        for id, _, _, amount in self.trans:
            if self.refundAmount == 0:
                return res
            amount -= self.map[id]
            
            if self.refundAmount >= amount:
                res.append([id, str(amount)])
                self.refundAmount -= amount
            else:
                res.append([id, str(self.refundAmount)])
                return res
        return res
