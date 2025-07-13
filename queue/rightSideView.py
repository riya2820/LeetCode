# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: 
            return []
        
        queue = deque([root])
        result = []
        currlevel = []
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                currlevel.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(currlevel[-1])
            currlevel = []
        
        return result
