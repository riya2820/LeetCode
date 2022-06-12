# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # using two pointers
        # insert dummy node 0
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # left and right pointer at a distance of n
        while right and n>0:
            right = right.next
            n -= 1
            
        while right != None:
            left = left.next
            right = right.next
            
        left.next = left.next.next # skips the nth element
        return dummy.next # this so we don't include dummy node 
