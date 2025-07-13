# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # optimized method pointers; no additional space/array required 
        # Time O(N)
        # Space O(1) 
        
        p1 = p2 = head
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            
        return p1
            
        
