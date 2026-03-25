from typing import List, Tuple

def maxDistToClosest(seats):
    max_dist = 0
    res_idx = -1
    prev = -1
    n = len(seats)

    for i in range(n):
        # leading zeros
        if seats[i] == 1:
            if prev == -1:
                if i > max_dist:
                    max_dist = i
                    res_idx = 0
            else:
                # middle zeros
                dist = (i - prev) // 2
                if dist > max_dist:
                    max_dist = dist
                    res_idx = prev + dist
            prev = i
    # trailing zeros
    if n - 1 - prev > max_dist:
        max_dist = n - 1 - prev
        res_idx = n - 1
    return max_dist, res_idx

seats = [1, 0, 0, 0, 1, 0, 1]
print(maxDistToClosest(seats))
seats = [1, 0, 0, 0,]
print(maxDistToClosest(seats))
