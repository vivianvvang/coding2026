
def set_usage():
    s = set()
    nums = [1, 2, 2, 3]
    s = set(nums)
    s.add(5)
    s.discard(1)
    to_remove = 2
    if to_remove in s:
        s.remove(2)

from collections import deque
def deque_usage():
    q = deque([1, 2, 3])
    q.append(4)
    q.pop() # pop from last
    q.appendleft(0)
    q.popleft() #O(1)

    first = q[0]
    last = q[-1]
    len = len(q)

from collections import Counter
# subclass of dict
def counter():
    nums = [1, 1, 2, 3]
    c = Counter(nums)
    # Counter({1: 2, 2: 1, 3: 1})
    get_index_0 = c[0] #O(1)
    print(c[1]) # return 2
    print(c[4]) # return 0, NO ERROR
    top2 = c.most_common(2) # return [(1, 2), (2, 1)]
    print(c.keys)