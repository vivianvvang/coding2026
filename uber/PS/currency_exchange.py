from typing import DefaultDict, List, Optional
"""

["GBP", "USD", "USD", "USD", "CNY"]
["JPY", "JPY", "GBP", "CAD", "EUR"]
 155.0, 112.0,  0.9,   1.3,  0.14]
"""
class CurrencyConverter:
    def __init__(self, fromArr: List[str], toArr: List[str], rateArr: List[float]):
        self.curr_map = DefaultDict(list)
        self.currency = {}
        # insert two way edges
        for i in range(len(fromArr)):
            f = fromArr[i]
            to = toArr[i]
            rate = rateArr[i]

            self.curr_map[f].append(to)
            self.curr_map[to].append(f)

            self.currency[f+to] = rate
            self.currency[to+f] = 1/rate
        
    def getBestRate(self, fr: str, to: str) -> float:
        res = -1
        def _backtrack(visited, node, goal, curr_rate):
            nonlocal res
            if node in visited:
                return
            if node == goal:
                res = max(res, round(curr_rate,3))
            visited.add(node)
            for nei in self.curr_map[node]:
                if node+nei not in self.currency:
                    continue
                _backtrack(visited, nei, goal, curr_rate * self.currency[node + nei])
            visited.remove(node)

        _backtrack(set(), fr, to, 1)
        return res

fromArray = ["GBP","USD","USD","USD","CNY"]
toArray = ["JPY","JPY","GBP","CAD","EUR"]
rateArray = [155,112,0.9,1.3,0.14]
currencyConventer = CurrencyConverter(fromArray, toArray, rateArray)

print(currencyConventer.getBestRate("USD", "JPY"))
