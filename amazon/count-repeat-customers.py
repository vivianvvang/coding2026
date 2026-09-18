def countRepeatCustomers(logs):
    first_visit = {}
    repeated = set()

    for customer, date in logs:
        if customer in repeated:
            continue
        if customer not in first_visit:
            first_visit[customer] = date
        elif first_visit[customer] != date:
            repeated.add(customer)
    return len(repeated)