# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
       
        def d(root):
            if not root:
                return 0
            
            l = d(root.left)
            r = d(root.right)
            
            if abs(l-r) > 1:
                self.result = False
                return False
            
            return max(l,r) + 1
        
        self.result = True
        d(root)
        return self.result
