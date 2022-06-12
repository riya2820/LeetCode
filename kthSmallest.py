# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Recursive soln
        # O(N) space and time complexity 
        def inorder(r):
            if r:
                return inorder(r.left) + [r.val] + inorder(r.right)
            else:
                return []
          
        return inorder(root)[k-1] #k-th smallest eleement
