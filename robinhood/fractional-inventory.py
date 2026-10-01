def fractionInvent(
    orders: List[List[str]],
    inventory: List[List[str]]
) -> List[List[str]]:

    # Store quantities in hundredths of a share to avoid floats.
    inventory_dict = {
        symbol: int(amount) for symbol, amount in inventory
    }

    for symbol, order_type, quantity, unit_price in orders:
        if quantity.startswith("$"):
            # Convert cents to hundredths of a share.
            # Integer division truncates any smaller fraction.
            shares = int(quantity[1:]) * 100 // int(unit_price)
        else:
            shares = int(quantity)

        current_inventory = inventory_dict.get(symbol, 0)

        if order_type == "B":
            # Customer buys: the broker gives shares from inventory.
            current_inventory -= shares
        else:
            # Customer sells: the broker receives shares.
            current_inventory += shares

        # Keep only the fractional share.
        # For negative values, Python's modulo also accounts for
        # buying enough whole shares to cover the shortfall.
        inventory_dict[symbol] = current_inventory % 100

    return [
        [symbol, str(inventory_dict[symbol])]
        for symbol in sorted(inventory_dict)
    ]
    
orders = [["AAPL", "B", "42", "100"], ["GOOG", "S", "$80", "160"]]
inventory = [["AAPL", "99"], ["GOOG", "60"]]
print(fractionInvent(orders, inventory))
orders = [["AAPL","B","$42","100"]]
inventory = [["AAPL","50"]]
print(fractionInvent(orders, inventory))
orders = [["AAPL","S","75","100"]]
inventory = [["AAPL","60"]]
print(fractionInvent(orders, inventory))
