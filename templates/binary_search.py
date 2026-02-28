# https://leetcode.com/discuss/post/786126/python-powerful-ultimate-binary-search-t-rwv8/

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    """
    Correctly initialize the boundary variables left and right to specify search space. 
    Only one rule: set up the boundary to include all possible elements;
    """
    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    """
    Consider whether to return left or left -1
    """
    return left