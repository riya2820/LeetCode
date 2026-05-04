from collections import deque

#  1
# 2  3   -> [1,3,4] 
#  5   4 
def rightSideView(self, root):
    if not root:
        return []

    result = []
    queue = deque([root]) # 1 

    while queue:
        level = []

        for _ in range(len(queue)): # 1
            node = queue.popleft()  # 1

            # add node value to level
            level.append(node.val)


            # add left/right children if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # after the for loop, append the last value from level
        result.append(level[-1])

    return result