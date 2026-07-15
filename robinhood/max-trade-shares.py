import heapq

def findMaxTradeShares(orders):
    buy = [] # max heap
    sell = [] # min heap
    trade = 0

    for order in orders:
        price, quantity, ot = int(order[0]), int(order[1]), order[2]
        if ot == "buy":
            while sell and quantity > 0:
                p, q = sell[0]
                if p <= price: 
                    temp_trade = min(quantity, q)
                    q -= temp_trade
                    trade += temp_trade
                    quantity -= temp_trade
                    if q == 0:
                        heapq.heappop(sell)
                    else:
                        sell[0] = (p, q)
                else:
                    break
            if quantity > 0:
                heapq.heappush(buy, (-price, quantity))
        else:
            while buy and quantity > 0:
                p, q = -buy[0][0], buy[0][1]
                if p >= price:
                    temp_trade = min(quantity, q)
                    q -= temp_trade
                    trade += temp_trade
                    quantity -= temp_trade
                    if q == 0:
                        heapq.heappop(buy)
                    else:
                        buy[0] = (-p, q)
                else:
                    break
            if quantity > 0:
                heapq.heappush(sell, (price, quantity))
    return trade

orders = [["150","5","buy"],["190","1","sell"],["200","1","sell"],["100","9","buy"],["140","8","sell"],["210","4","buy"]]
print(findMaxTradeShares(orders))