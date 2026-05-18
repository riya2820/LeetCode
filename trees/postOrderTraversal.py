class Solution:
    def postorderTraversal(self, root): 
        if not root:
            return []

        result = []

        if root:
            result.append(root.val)
            self.postrderTraversal(root.left)
            self.postorderTraversal(root.right)

        return result 

A = Solution()
root = [1,2,3,4,5,null,8,null,null,6,7,9]
root = Node(10)
root.left = Node(5)
root.right = Node(15)
print(A.postorderTraversal(root))