from typing import List, Optional
from collections import Counter

class Solution:
    def exactTradeMatch(self, house: List[str], street: List[str]) -> List[str]:
        # Count occurrences of each trade in both lists.
        house_counter = Counter(house)
        street_counter = Counter(street)

        # For every trade present in both, remove the matching pairs.
        for trade in list(house_counter.keys() & street_counter.keys()):
            matches = min(house_counter[trade], street_counter[trade])
            house_counter[trade] -= matches
            street_counter[trade] -= matches
            if house_counter[trade] == 0:
                del house_counter[trade]
            if street_counter[trade] == 0:
                del street_counter[trade]

        # Combine the remaining unmatched trades.
        unmatched = list(house_counter.elements()) + list(street_counter.elements())
        return sorted(unmatched)
    


# Follow up
from collections import defaultdict, deque
from typing import List


class Solution:
    def getUnmatchTrades(
        self,
        house: List[str],
        street: List[str]
    ) -> List[str]:

        def remove_cross_matches(house, street, match_type):
            """
            Remove matches between house and street.

            exact: symbol, side, quantity, id 都相同
            attribute: symbol, side, quantity 相同，忽略 id
            """

            street_map = defaultdict(deque)

            # 排序后放进去，保证处理顺序稳定
            for trade in sorted(street):
                parts = trade.split(",")

                if match_type == "exact":
                    key = trade
                else:
                    key = (parts[0], parts[1], parts[2])

                street_map[key].append(trade)

            remaining_house = []

            for trade in sorted(house):
                parts = trade.split(",")

                if match_type == "exact":
                    key = trade
                else:
                    key = (parts[0], parts[1], parts[2])

                if street_map[key]:
                    # 找到一个 street trade，两个一起删除
                    street_map[key].popleft()
                else:
                    remaining_house.append(trade)

            # street_map 中剩下的就是没有匹配到的 street trades
            remaining_street = []

            for trades in street_map.values():
                remaining_street.extend(trades)

            return remaining_house, remaining_street

        def remove_offsets(trades):
            """
            在同一个列表内部：
            相同 symbol、quantity，买卖方向相反时互相抵消。
            """

            groups = defaultdict(lambda: {"B": [], "S": []})

            for trade in trades:
                symbol, side, quantity, trade_id = trade.split(",")
                groups[(symbol, quantity)][side].append(trade)

            remaining = []

            for group in groups.values():
                buys = sorted(group["B"])
                sells = sorted(group["S"])

                match_count = min(len(buys), len(sells))

                # 最早的 buy 和最早的 sell 被抵消
                remaining.extend(buys[match_count:])
                remaining.extend(sells[match_count:])

            return remaining

        # 1. Exact match
        house, street = remove_cross_matches(
            house,
            street,
            "exact"
        )

        # 2. Attribute match
        house, street = remove_cross_matches(
            house,
            street,
            "attribute"
        )

        # 3. Offset match，只能在同一个列表内部进行
        house = remove_offsets(house)
        street = remove_offsets(street)

        return sorted(house + street)

