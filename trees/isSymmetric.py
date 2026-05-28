# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # Recursive Solution 
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True # i.e reached end; tree is symmetric 
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
        
        return isMirror(root.left, root.right)
        