class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # O(N) time complexity 
        prev = None
        
        while head:
            temp = head
            head = head.next 
            temp.next = prev 
            prev = temp
        return prev 
            
            
        
