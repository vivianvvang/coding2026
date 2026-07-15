def fractionInvent(orders, inventory):
    inventory_dict = {}
    for symbol, amount in inventory:
        inventory_dict[symbol] = int(amount)
    for symbol, order, quantity, up in orders:
        price = int(up)
        if quantity.startswith("$"):
            dollar_amount = int(quantity[1:])
            shares = dollar_amount * 100 // price
        else:
            shares = int(quantity)
        
        current_inventory = inventory_dict.get(symbol, 0)
        
        if order == "B":
            current_inventory -= shares
        else:
            current_inventory += shares
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
