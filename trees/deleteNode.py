# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # O(N) time complexity 
        
        # edge case
        if not root:
            return None
        
                
        if root.val > key:
            root.left = self.deleteNode(root.left, key) # search in left subtree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key) # search in right subtree
       
        else: # i.e root.val == key 
            # 4 possibilities
            if not root.right and not root.left:
                return None
            if root.left and not root.right:
                return root.left
            if root.right and not root.left:
                return root.right
            else:
                point = root.right
                while point.left: 
                    point = point.left
                root.val = point.val
                root.right = self.deleteNode(root.right, root.val)
          
        return root
                
                
