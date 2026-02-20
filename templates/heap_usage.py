import heapq

data = [5, 1, 8, 3, 2]
heapq.heapify(data)
print(data)

heapq.heappush(data, 0)

pop_min = heapq.heappop(data)
smallest = heapq[0]

# heapq with tuple element:
# WARNING: If costs are equal, Python tries to compare Node vs Node and will CRASH.
# Try add index or other identicle 