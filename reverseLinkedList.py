# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # O(N) time complexity 
        #reversedLL = ListNode()
        prev = None

        while (head != None):
            next_temp = head.next         
            head.next = prev
            prev = head
            head = next_temp
        return prev
            
            
