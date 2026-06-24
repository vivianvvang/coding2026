
# You are given an array P which is a permutation of numbers from 1 to N
# and an integer k.Your task is to determine if
# return true if: for every integer x from 1 to k
# the set of numbers {1, 2, ..., x} forms a contiguous subarray within P
"""
Example 1:
P = [3, 1, 2, 5, 4], k = 3, Res = True
x = 1: {1}
x = 2: {1, 2}
x = 3: {3, 1, 2}

Example 2:
P = [1, 3, 2, 4], k = 2, Res = False
x = 1: {1}
x = 2: Not exist
"""

def check_k_permutations(list: list[int], k: int) -> bool:
    n = len(list)
    if k > n: 
        return False
    
    pos = [0] * (n + 1)
    for i, val in enumerate(list):
        pos[val] = i
    curr_min = float('inf')
    curr_max = float('-inf')

    for x in range(1, k + 1):
        idx = pos[x]
        curr_min = min(curr_min, idx)
        curr_max = max(curr_max, idx)
        if curr_max - curr_min + 1 != x:
            return False
    return True
# --- Test Cases ---
print(check_k_permutations([3, 1, 2, 5, 4], 3)) # True
print(check_k_permutations([1, 3, 2, 4], 2))    # False (1..2 are at indices 0,2 -> length 3 != 2)
        