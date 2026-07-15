from typing import List, Optional
import heapq


def portValOptimization(m: int, sec: List[List[str]]) -> float:
    candidates = []
    
    for symbol, str_price, predict_str, amount_str in sec:
        price, predict, amount = int(str_price), int(predict_str), int(amount_str)
    
        if predict <= price:
            continue
        candidates.append((predict/price, price, predict, amount))
    candidates.sort(key=lambda candidate: candidate[0], reverse = True)

    res = 0
    for ratio, price, predict, amount in candidates:
        max_cost = price * amount
        cost = min(m, max_cost)

        shares = cost / price
        m -= cost
        res = res + predict * shares
        
        if m == 0:
            break
    return res + m

"""
What strategies would you use to handle floating-point rounding errors 
in real-world financial systems?

- For currencies with two decimal places, store cents rather than dollars
- Keep high precision during intermediate calculations
--------------------------------------------------------------------
"""
m = 50
sec = [
    ["SNAP", "20", "30", "5"],
    ["AAPL", "50", "70", "2"]
]
print(portValOptimization(m, sec))

assert portValOptimization(
    100,
    [["AAPL", "15", "10", "3"], ["BYND", "40", "35", "3"]]
) == 100

# Budget only allows a fractional share
assert portValOptimization(
    10,
    [["AAPL", "20", "40", "5"]]
) == 20

# Enough money to buy all profitable shares; leftover cash remains
assert portValOptimization(
    100,
    [["AAPL", "10", "20", "2"]]
) == 120

# No gain when future and current prices are equal
assert portValOptimization(
    50,
    [["AAPL", "10", "10", "5"]]
) == 50

m = 100
sec = [["AAPL", "15", "10", "3"], ["BYND", "40", "35", "3"]]
print(portValOptimization(m, sec))

m = 50
sec = [["SNAP", "20", "30", "5"], ["AAPL", "50", "70", "2"]]
print(portValOptimization(m, sec))

