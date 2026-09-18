
def smallestSafeDigitRearrangement(s: str) -> str:
    counts = [0] * 10
    for char in s:
        counts[int(char)] += 1
    memo = {}

    def dfs(remaining, prev):
        node = (remaining, prev)
        if node in memo:
            return memo[node]

        if not any(remaining):
            # Can reach to this point but no digit remains
            return ""

        for digit in range(10):
            if remaining[digit] == 0:
                continue
            if prev != -1 and prev + digit > 9:
                continue

            remaining_take = list(remaining)
            remaining_take[digit] -= 1
            remaining_take = tuple(remaining_take) # for memo dict key

            future_res = dfs(remaining_take, digit)
            if future_res is not None:
                result = str(digit) + future_res
                memo[node] = result
                return result

        memo[node] = None
        return None

    res = dfs(tuple(counts), -1)
    return res if res is not None else ""


    

print(smallestSafeDigitRearrangement('9081'))