#
# @lc app=leetcode id=1428 lang=python3
#
# [1428] Leftmost Column with at Least a One
#

# @lc code=start
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

    def leftMostColumnWithOne_binary_search(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Mlog(N)
        m, n = binaryMatrix.dimensions()
        ans = n + 1

        def binary_search(i):
            l, r  = 0, n - 1
            while l < r:
                mid = l + (r - l) // 2

                if binaryMatrix.get(i, mid) == 1:
                    r = mid
                else:
                    l = mid + 1
            if(binaryMatrix.get(i, l) == 0):
                return n + 1
            return l
    
        for i in range(m):
            first_one = binary_search(i)
            ans = min(first_one, ans)
        if ans > n: 
            return -1 
        return ans
            
    # linear
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        r, c = 0, n - 1
        res = n + 1
        while r < m and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                # continue the search on that row
                res = min(c, res)
                c -= 1
            else:
                # leftmost 1 can't be to the left of it.
                r += 1
        if res > n:
            return -1
        return res


        
# @lc code=end

