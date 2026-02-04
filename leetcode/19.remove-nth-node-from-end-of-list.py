#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
# Two pointers approach: first pointer advances n steps ahead
# once first pointer reaches the end, second pointer will be at the nth to last node
# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        first, second = dummy, dummy

        for _ in range(n):
            first = first.next
        while first.next is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

        
# @lc code=end

