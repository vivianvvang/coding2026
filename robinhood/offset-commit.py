def commitOffset(offsets):
    next_to_commit = 0
    waiting = set()
    result = []

    for offset in offsets:
        waiting.add(offset)

        if next_to_commit in waiting:
            while next_to_commit in waiting:
                waiting.remove(next_to_commit)
                next_to_commit += 1
            result.append(next_to_commit - 1)
        else:
            result.append(-1)

    return result

print(commitOffset([2, 0, 1]))
# [-1, 0, 2]

print(commitOffset([0, 1, 2]))
# [0, 1, 2]

print(commitOffset([2, 1, 0, 5, 4]))
# [-1, -1, 2, -1, -1]

"""
How would you adapt this logic if offsets were sparse and 
spanned a very large integer range?
- TreeMap Time: O(NlogK)
"""

"""
What synchronization mechanisms would be required to safely 
run this in a multi-threaded producer-consumer setup?
1. Protecting shared state (waiting set, highestCommitted, results) from race conditions.
2. Ordering/Coordination: Ensuring that the "commit" logic only proceeds when the necessary preceding messages have actually arrived, while allowing out-of-order processing.
"""