# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # O(N) time 
        # solve using O(1) constant memory 
        p1 = p2 = head 
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            
            if p1 == p2: # cycle deteced! 
                return True
            
        return False
