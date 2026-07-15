from collections import defaultdict

def buildPortfolio(trades):
    cash = 1000
    p = defaultdict(int)
    for _, symbol, d, quantity, price in trades:
        if d == "B":
            p[symbol] += int(quantity)
            cash -= int(quantity) * int(price)
        else:
            p[symbol] -= int(quantity)
            cash += int(quantity) * int(price)
    res = [
        [symbol, str(quantity)]
        for symbol, quantity in p.items()
        if quantity > 0    
    ]
    res.sort(key = lambda position: position[0])
    return [["CASH", str(cash)]] + res


"""
If trades arrived as a continuous stream
how would you design this system for real-time updates
"""
trades = [["1", "AAPL", "B", "10", "10"], ["3", "GOOG", "B", "20", "5"], ["10", "AAPL", "S", "10", "15"]]
print(buildPortfolio(trades))

trades = [["1", "AAPL", "B", "10", "10"], ["3", "GOOG", "B", "20", "5"], ["10", "AAPL", "S", "5", "15"]]
print(buildPortfolio(trades))

from typing import Dict, List, Any
def format_money(value: float) -> str:
    return f"{value:.2f}"

import heapq

def marginCall(trades):
    cash = 1000
    holdings = defaultdict(int)
    latest_price = defaultdict(int)
    version = defaultdict(int)
    price_heap = []

    for _, symbol, direction, quantity, price in trades:
        quantity = int(quantity)
        price = int(price)

        version[symbol] += 1
        latest_price[symbol] = price
        heapq.heappush(price_heap, (-price, symbol, version[symbol]))

        if direction == "B":
            holdings[symbol] += quantity
            cash -= quantity * price
        else:
            holdings[symbol] -= quantity
            cash += quantity * price

        while cash < 0:
            while price_heap:
                negative_price, sell_symbol, entry_version = price_heap[0]

                if (
                    entry_version == version[sell_symbol]
                    and holdings[sell_symbol] > 0
                ):
                    break

                heapq.heappop(price_heap)

            negative_price, sell_symbol, entry_version = heapq.heappop(price_heap)
            sell_price = -negative_price

            deficit = -cash
            shares_needed = (deficit + sell_price - 1) // sell_price
            shares_to_sell = min(
                shares_needed,
                holdings[sell_symbol]
            )

            holdings[sell_symbol] -= shares_to_sell
            cash += shares_to_sell * sell_price

            if holdings[sell_symbol] > 0:
                heapq.heappush(price_heap, (-sell_price, sell_symbol, entry_version))

    portfolio = [["CASH", str(cash)]]

    for symbol in sorted(holdings):
        if holdings[symbol] > 0:
            portfolio.append([symbol, str(holdings[symbol])])

    return portfolio


def collateral(trades: List[List[str]]) -> List[List[str]]:
    cash = 1000

    holdings = {}
    latest_price = {}
    version = {}

    # Entries: (-price, symbol, version)
    sell_heap = []

    def is_special(symbol):
        return symbol.endswith("O")

    def collateral_symbol(symbol):
        return symbol[:-1]

    def liquid_shares(symbol):
        owned = holdings.get(symbol, 0)

        if is_special(symbol):
            return owned

        special_symbol = symbol + "O"
        collateral_required = holdings.get(special_symbol, 0)

        return owned - collateral_required

    def refresh(symbol):
        """
        Invalidate older heap entries for this symbol and add a fresh
        entry if the symbol currently has sellable shares.
        """
        version[symbol] = version.get(symbol, 0) + 1

        if symbol in latest_price and liquid_shares(symbol) > 0:
            heapq.heappush(
                sell_heap,
                (
                    -latest_price[symbol],
                    symbol,
                    version[symbol]
                )
            )

    def cover_margin():
        nonlocal cash

        while cash < 0:
            # Remove stale or currently unsellable entries.
            while sell_heap:
                negative_price, symbol, entry_version = heapq.heappop(
                    sell_heap
                )

                if (
                    entry_version == version.get(symbol, 0)
                    and -negative_price == latest_price.get(symbol)
                    and liquid_shares(symbol) > 0
                ):
                    break
            else:
                raise ValueError("Portfolio cannot cover the margin call")

            price = -negative_price
            available = liquid_shares(symbol)
            deficit = -cash

            shares_needed = (deficit + price - 1) // price
            shares_to_sell = min(available, shares_needed)

            holdings[symbol] -= shares_to_sell
            cash += shares_to_sell * price

            # The sold symbol's availability changed.
            refresh(symbol)

            # Selling a special stock releases collateral shares.
            if is_special(symbol):
                refresh(collateral_symbol(symbol))

    for _, symbol, direction, quantity, price in trades:
        quantity = int(quantity)
        price = int(price)

        holdings.setdefault(symbol, 0)
        latest_price[symbol] = price

        if direction == "B":
            holdings[symbol] += quantity
            cash -= quantity * price

            if is_special(symbol):
                collateral = collateral_symbol(symbol)

                if holdings.get(collateral, 0) < holdings[symbol]:
                    raise ValueError(
                        "Not enough collateral for special-stock purchase"
                    )

        else:
            if is_special(symbol):
                if holdings[symbol] < quantity:
                    raise ValueError("Invalid sell")
            else:
                if liquid_shares(symbol) < quantity:
                    raise ValueError("Cannot sell collateral shares")

            holdings[symbol] -= quantity
            cash += quantity * price

        refresh(symbol)

        # Trading a special stock also changes how much collateral is free.
        if is_special(symbol):
            refresh(collateral_symbol(symbol))

        if cash < 0:
            cover_margin()

    result = [["CASH", str(cash)]]

    for symbol in sorted(holdings):
        if holdings[symbol] > 0:
            result.append([symbol, str(holdings[symbol])])

    return result


def build_portfolio_with_cost_basis(trades) -> Dict[str, Any]:

    cash = 1000.0
    positions = defaultdict(
        lambda: {
            "quantity": 0,
            "total_cost": 0.0,
            "realized_gain": 0.0
        }
    )

    rejected_trades = []

    for trade in trades:
        _, symbol, direction, quantity_str, price_str = trade

        try:
            quantity = int(quantity_str)
            price = float(price_str)
        except ValueError:
            rejected_trades.append({
                "trade": trade,
                "reason": "Invalid quantity or price"
            })
            continue

        if quantity < 0 or price < 0:
            rejected_trades.append({
                "trade": trade,
                "reason": "Quantity and price must be non-negative"
            })
            continue

        position = positions[symbol]
        trade_value = quantity * price

        if direction == "B":
            if cash < trade_value:
                rejected_trades.append({
                    "trade": trade,
                    "reason": "Insufficient cash"
                })
                continue

            cash -= trade_value

            position["quantity"] += quantity
            position["total_cost"] += trade_value

        elif direction == "S":
            if position["quantity"] < quantity:
                rejected_trades.append({
                    "trade": trade,
                    "reason": "Insufficient shares"
                })
                continue

            # 必须在减少 quantity 之前计算平均成本
            average_cost = (
                position["total_cost"] / position["quantity"]
                if position["quantity"] > 0
                else 0.0
            )

            sale_proceeds = quantity * price
            sold_cost = quantity * average_cost
            realized_gain = sale_proceeds - sold_cost

            cash += sale_proceeds

            position["quantity"] -= quantity
            position["total_cost"] -= sold_cost
            position["realized_gain"] += realized_gain

            # 全部卖完后清零，避免出现极小的浮点数误差
            if position["quantity"] == 0:
                position["total_cost"] = 0.0

        else:
            rejected_trades.append({
                "trade": trade,
                "reason": "Invalid direction"
            })

    portfolio = [["CASH", format_money(cash)]]
    realized_gains = []

    for symbol in sorted(positions):
        position = positions[symbol]
        quantity = position["quantity"]

        if quantity > 0:
            average_cost = position["total_cost"] / quantity

            portfolio.append([
                symbol,
                str(quantity),
                format_money(average_cost),
                format_money(position["total_cost"])
            ])

        realized_gains.append([
            symbol,
            format_money(position["realized_gain"])
        ])

    total_realized_gain = sum(
        position["realized_gain"]
        for position in positions.values()
    )

    return {
        # 每行：
        # [symbol, quantity, average_cost, remaining_cost_basis]
        "portfolio": portfolio,

        # 每行：
        # [symbol, realized_gain]
        "realized_gains": realized_gains,

        "total_realized_gain": format_money(total_realized_gain),
        "rejected_trades": rejected_trades
    }