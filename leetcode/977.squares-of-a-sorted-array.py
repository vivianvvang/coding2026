class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        r = n - 1
        for i in range(n):
            if nums[i] >= 0:
                r = i
                break
        l = r - 1
        while 0 <= l < n or 0 <= r < n:
            if l < 0:
                res.append(nums[r] ** 2)
                r += 1
            elif r >= n:
                res.append(nums[l] ** 2)
                l -= 1
            else:
                sl, sr = nums[l] ** 2, nums[r] ** 2
                if sl <= sr:
                    res.append(sl)
                    l -= 1
                else:
                    res.append(sr)
                    r += 1
        return res

        