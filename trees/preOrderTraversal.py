class Solution:
    def preorderTraversal(self, root): 
        if not root:
            return []

        result = []

      
        result.append(root.val)
        result.append(self.preorderTraversal(root.left))
        result.append(self.preorderTraversal(root.right))

        return result 

A = Solution()
root = [1,2,3,4,5,null,8,null,null,6,7,9]
root = Node(10)
root.left = Node(5)
root.right = Node(15)
print(A.preorderTraversal(root))