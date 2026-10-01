from typing import List, Optional
import heapq
class Solution:
    def findMaxTradeShares(self, orders: List[List[str]]) -> int:
        
        buy = [] # max heap
        sell = [] # min heap
        trade = 0

        for order in orders:
            price, quantity, ot = int(order[0]), int(order[1]), order[2]
            if ot == "buy":
                while sell and quantity > 0:
                    sp, sq = sell[0]
                    #sell price is less than or equal to the buy price.
                    if sp <= price: 
                        temp_trade = min(quantity, sq)
                        sq -= temp_trade
                        trade += temp_trade
                        quantity -= temp_trade
                        if sq == 0:
                            heapq.heappop(sell)
                        else:
                            sell[0] = (sp, sq)
                    else:
                        break
                if quantity > 0:
                    heapq.heappush(buy, (-price, quantity))
            else:
                while buy and quantity > 0:
                    bp, bq = -buy[0][0], buy[0][1]
                    #A sell order can be matched with a buy order if the buy price is greater than or equal to the sell price.
                    if bp >= price:
                        temp_trade = min(quantity, bq)
                        bq -= temp_trade
                        trade += temp_trade
                        quantity -= temp_trade
                        if bq == 0:
                            heapq.heappop(buy)
                        else:
                            buy[0] = (-bp, bq)
                    else:
                        break
                if quantity > 0:
                    heapq.heappush(sell, (price, quantity))
        return trade


    # TIME: O(NlogN) Each order might involve several heap operations (insertion and deletion) that take O(log N) time.
    # SPACE: O(N)