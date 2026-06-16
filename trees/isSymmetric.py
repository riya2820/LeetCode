# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root): 
        if not root:
            return []

        result = []
        if root:
            result.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        
        return result

    def postorderTraversal(self, root): 
        if not root:
            return []

        result = []
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            result.append(root.val)
        return result

    
    def inorderTraversal(self, root): 
        if not root:
            return []

        result = []
        if root:
            self.inorderTraversal(root.left)
            result.append(root.val)
            self.inorderTraversal(root.right)
        return result

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        #     1         
        #  2      2  
        # 4 5    5 4  

        def mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1 and t2 and t1.val != t2.val:
                return False       
            return mirror(t1.left, t2.right) and mirror(t1.right, t2.left)  

        return self.isSymmetric(root.left, root.right)


    def isBalanced(self, root):
        if not root:
            return
        
        return 
    # root = [3,9,20,null,null,15,7]

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not root:
            return False
        pass

    def maxDepth(self, root):
        if not root:
            return 0
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(leftHeight, rightHeight) + 1 


    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.left == None:
            return self.minDepth(root.right) + 1
        elif root.right == None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        '''
        if not root:
            return 0
        
        def dfs(root):
            if not root.left:
                return dfs(root.right) + 1
            if not root.right:
                return dfs(root.left) + 1
            return min(dfs(root.left), dfs(root.right)) + 1
        
        return dfs(root) '''



'''
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
        
        return isMirror(root.left, root.right)'''
        