# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # O(N) time and O(N) space complexity 
        # edge case
        if not head:
            return None
    
        # odd and even pointer
        odd = head
        even = head.next
        odd, even = head, head.next

        evenHead = even
        
        #edge case of boundary limits
        while (odd and even and odd.next and even.next):
            #next pointer of odd LL should point to next node of even indexed node
            odd.next = even.next
            #shift the odd pointer
            odd = odd.next
            #next pointer of even LL should point to next node of odd indexed node
            even.next = odd.next
            #shift the even pointer
            even = even.next
        #join end of odd LL with the head of even LL
        odd.next = evenHead
        return head
        
