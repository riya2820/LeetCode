# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def extract_nums(l1):
	"""
		type l1: linked list
	"""
	temp = l1
	num = ''
	while temp != None:
		num = str(temp.val) + num # stores in reverse format.
		temp = temp.next
	return int(num) #returns the integer

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        S = str(extract_nums(l1) + extract_nums(l2))
        head = ListNode(int(S[-1]))
        temp = head
        
        for i in S[-2::-1]:
            num = int(i)
            temp.next = ListNode(num)
            temp = temp.next
        
        return head
