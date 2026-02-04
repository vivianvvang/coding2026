#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
import heapq
from typing import Optional, List

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        head = dummy
        min_heap = []

        for i in range(len(lists)):
            l = lists[i]
            if l is not None:
                # WARNING: If costs are equal, Python tries to compare Node vs Node and will CRASH.
                heapq.heappush(min_heap, (l.val, i, l))
        while len(min_heap) > 0:
            _, idx, min = heapq.heappop(min_heap)
            head.next = min
            head = head.next
            if min.next is not None:
                heapq.heappush(min_heap, (min.next.val, idx, min.next))
        return dummy.next


        
# @lc code=end

