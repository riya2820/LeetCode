# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        current = head
        if (current != Nonea and current.next != None):
            if (current.next.val == current.val):
                current.next = current.next.val 
            else:
                current = current.next
        return head
        """

        if head: 
            curr_val, node = head.val, head
            while node.next:
                if node.next.val == curr_val:
                    node.next = node.next.next
                else:
                    curr_val = node.next.val
                    node = node.next
        return head
