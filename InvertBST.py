class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invertRoot(root):
            if root == None:
                return None
            else:
                root.left, root.right = root.right, root.left
                invertRoot(root.left)
                invertRoot(root.right)
        
        invertRoot(root)
        return root
        
