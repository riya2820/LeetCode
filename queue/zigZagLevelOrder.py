# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        result = []
        zigZag = True
        if not root: # edge case!
            return None
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []            
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            
            if zigZag:
                result.append(level)
                zigZag = False
            else:
                result.append(level[::-1]) # append in reverse order i.e zigZag 
                zigZag = True
            
        return result
                
                
                
