import collections
import math
'''
给正整数 n, 一次操作可以让 n = n ± 2^i (i ≥ 0)。求把 n 变成 0 的最少操作次数。
'''
def minOpeator(n):
    res = 0
    while n:
        if n%2 == 0:
            n>>=1
        else:
            if n%4 == 3:
                n+=1
            else:
                n-=1
            res+=1
    return res
print(minOpeator(1))
print(minOpeator(15))
print(minOpeator(8))
print(minOpeator(7))
print(minOpeator(6))