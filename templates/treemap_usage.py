from sortedcontainers import SortedDict

# Works exactly like a Kotlin TreeMap
sd = SortedDict()

# 2. Insertions - O(log N)
sd[30] = "Thirty"
sd[10] = "Ten"
sd[40] = "Forty"
sd[20] = "Twenty"
# Notice it prints in order by key {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
print(f"Current State: {sd}")

del sd[20] # O(log N)
