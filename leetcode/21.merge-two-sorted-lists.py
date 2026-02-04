#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        h1, h2 = list1, list2
        
        while h1 and h2:
            if h1.val <= h2.val:
                head.next = h1
                h1 = h1.next
            else: 
                head.next = h2
                h2 = h2.next
            head = head.next
        head.next = h1 if h1 is not None else h2
        return dummy.next

        
# @lc code=end

