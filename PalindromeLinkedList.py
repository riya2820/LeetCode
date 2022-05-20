# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        vals = []
        currentNode = head
        while (currentNode != None):
            vals.append(currentNode.val)
            currentNode = currentNode.next
        
        return vals == vals[::-1]
