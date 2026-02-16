import collections
import math
'''
Given a positive integer n, you can apply  n = n ± 2^i (i ≥ 0)
Return the minimum number of operations needed for n to become 0
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

print(minOpeator(1)) #1
print(minOpeator(15)) #2
print(minOpeator(8)) #1
print(minOpeator(7)) #2 7 -> 8 -> 0
print(minOpeator(6)) #2 6 -> 8 -> 0