"""
NeetCode 150 — Graphs (grids) + Binary Trees  [PRACTICE STUBS]
Single file, runnable offline:  python3 neetcode_practice.py

Fill in each method. Tests at the bottom check your work — run the file to
see which pass. A failing/unimplemented method raises; tests stop there.

Problems:
  1. Count Number of Islands
  2. Max Area of Island
  3. Rotting Fruit
  4. Invert a Binary Tree
  5. Depth (Max Depth) of Binary Tree
  6. Binary Tree Diameter
  7. Same Binary Tree
  8. Subtree of a Binary Tree
  9. Level Order Traversal
 10. Binary Tree Right Side View
 11. Valid Binary Search Tree
"""

from collections import deque
from typing import List, Optional


# ----------------------------------------------------------------------
# Tree node + helper to build trees from a level-order list (LeetCode style)
# This is scaffolding — don't reimplement. Use build_tree in your own tests.
# ----------------------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a level-order list where None means 'no node'.
    Example: [1, 2, 3, None, 4] ->
            1
           / \
          2   3
           \
            4
    """
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals):
            if vals[i] is not None:
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i += 1
        if i < len(vals):
            if vals[i] is not None:
                node.right = TreeNode(vals[i])
                q.append(node.right)
            i += 1
    return root


class Solution:
    # ------------------------------------------------------------------
    # 1. Count Number of Islands  (grid of "0"/"1" strings)
    # HINT: scan every cell; each unvisited "1" = one new island, then
    #       flood-fill (DFS/BFS) the whole island so you don't recount it.
    # ------------------------------------------------------------------
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(r, c):
            # handle all edge cases
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
                return # exit helper function
            grid[r][c] = "-1" # recursively looks for all nearby cells, and markes them as visited
            dfs(r-1, c) # left
            dfs(r+1, c) # right
            dfs(r, c-1) # down
            dfs(r, c+1) # up

        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "-1" # mark visited
                    count += 1
                    dfs(r,c)

                    # up, down, left, right

        return count
    # ------------------------------------------------------------------
    # 2. Max Area of Island  (grid of 0/1 ints)
    # HINT: same flood-fill as #1, but have it RETURN the cell count so you
    #       can track the running max across islands.
    # ------------------------------------------------------------------
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        raise NotImplementedError

    # ------------------------------------------------------------------
    # 3. Rotting Fruit  (0 empty, 1 fresh, 2 rotten)
    # HINT: multi-source BFS — seed the queue with ALL rotten cells, also
    #       count fresh. Process the queue one layer (= one minute) at a
    #       time. Return -1 if fresh remain at the end.
    # ------------------------------------------------------------------
    def orangesRotting(self, grid: List[List[int]]) -> int:
        raise NotImplementedError

    # ------------------------------------------------------------------
    # 4. Invert a Binary Tree
    # HINT: swap left/right, recurse into both. Base case: empty node.
    # ------------------------------------------------------------------
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        def helper(root):
            if not root:
                return None
            root.left, root.right = root.right, root.left
            helper(root.left)
            helper(root.right)

        helper(root)
        return root # return the modifies TreeNode

    # ------------------------------------------------------------------
    # 5. Max Depth of Binary Tree
    # HINT: 1 + max(depth(left), depth(right)); empty node = 0.
    # ------------------------------------------------------------------
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        if not root.left:
            return self.maxDepth(root.right) + 1
        elif not root.right:
            return self.maxDepth(root.left) + 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # ------------------------------------------------------------------
    # 6. Binary Tree Diameter  (longest path between two nodes, in EDGES)
    # HINT: write a depth() helper; at each node the candidate diameter is
    #       depth(left)+depth(right). Track a max as a side effect while
    #       depth() returns 1+max(left,right) upward.
    # ------------------------------------------------------------------
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        raise NotImplementedError

    # ------------------------------------------------------------------
    # 7. Same Binary Tree
    # HINT: both empty -> True; one empty or vals differ -> False;
    #       else recurse left==left and right==right.
    # ------------------------------------------------------------------
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return True

    # ------------------------------------------------------------------
    # 8. Subtree of a Binary Tree
    # HINT: at each node of root, check isSameTree(node, subRoot); else
    #       recurse into left/right. Empty subRoot -> True; empty root -> False.
    # ------------------------------------------------------------------
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        raise NotImplementedError

    # ------------------------------------------------------------------
    # 9. Level Order Traversal  (BFS, grouped per level)
    # HINT: BFS with a queue; freeze len(queue) at the top of each loop to
    #       know how many nodes belong to the current level.
    # ------------------------------------------------------------------
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 

        # 3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
        q = deque([root])
        print("q=", q)
        result = []
        level = []
        # visited.add(q)

        while q: # [3]
            level = [] # []
            for _ in range(len(q)): # [9, 20]
                curr = q.popleft()  # 3
                level.append(curr.val) # [3] - > # [9]
                if curr.left:
                    q.append(curr.left) # [9] -> 
                if curr.right:
                    q.append(curr.right) # [9, 20]

            result.append(level) # [[3]]

            
        print("RESULT=", result)
        return result


    # ------------------------------------------------------------------
    # 10. Right Side View  (rightmost node value at each level)
    # HINT: level-order BFS; append the LAST node of each level (i == size-1).
    # ------------------------------------------------------------------
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        rightView = []

        while q:
            #for _ in range(len(q)):
            curr = q.popleft()
            rightView.append(curr.val)
            if curr.right:
                q.append(curr.right)

        return rightView


    # ------------------------------------------------------------------
    # 11. Valid Binary Search Tree
    # HINT: pass (low, high) bounds down. Each node must satisfy
    #       low < val < high; left tightens high to val, right tightens low.
    #       Start with (-inf, +inf).
    # ------------------------------------------------------------------
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        raise NotImplementedError


# ----------------------------------------------------------------------
# Tests — these encode the expected answers, so they double as the spec.
# Run the file; each line prints OK or the suite raises on the first failure.
# ----------------------------------------------------------------------
def run_tests():
    s = Solution()

    # 7. Same Tree
    assert s.isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True
    assert s.isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) is False
    assert s.isSameTree(None, None) is True

    # print(s.isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3]))) # is True
    # print(s.isSameTree(build_tree([1, 2]), build_tree([1, None, 2]))) # is False
    # print(s.isSameTree(None, None)) # is True
    print("7. isSameTree               OK")

    # 4. Invert Binary Tree
    inverted = s.invertTree(build_tree([1, 2, 3, 4, 5, 6, 7]))
    # assert s.invertTree(build_tree([1, 2, 3, 4, 5, 6, 7])) 
    # assert s.levelOrder(inverted) == [[1], [3, 2], [7, 6, 5, 4]]
    assert s.invertTree(None) is None
    print("4. invertTree               OK")


    # 5. Max Depth
    # assert s.maxDepth(build_tree([1, 2, 3, None, None, 4])) == 3
    print(s.maxDepth(build_tree([1, 2, 3, None, None, 4])))
    #assert s.maxDepth(None) == 0
    # assert s.maxDepth(build_tree([1])) == 1
    print("5. maxDepth                 OK")


    # 9. Level Order
    # assert s.levelOrder(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    print(s.levelOrder(build_tree([3, 9, 20, None, None, 15, 7])))
    # assert s.levelOrder(None) == []
    print(s.levelOrder(None))
    print("9. levelOrder               OK")

    # 10. Right Side View
    assert s.rightSideView(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    print(s.rightSideView(build_tree([1, 2, 3, 4])))
    # assert s.rightSideView(build_tree([1, 2, 3, 4])) == [1, 3, 4]
    assert s.rightSideView(None) == []
    print("10. rightSideView           OK")


    '''
    # 1. Count Number of Islands
    grid = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert s.numIslands(grid) == 4
    assert s.numIslands([["0"]]) == 0
    assert s.numIslands([["1"]]) == 1
    print("1. numIslands               OK") 

    
    # 2. Max Area of Island
    g = [
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
    ]
    assert s.maxAreaOfIsland(g) == 6
    assert s.maxAreaOfIsland([[0, 0], [0, 0]]) == 0
    print("2. maxAreaOfIsland          OK")


    # 3. Rotting Fruit
    assert s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert s.orangesRotting([[0, 2]]) == 0
    print("3. orangesRotting           OK")


    # 6. Diameter (in edges)
    assert s.diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])) == 3
    assert s.diameterOfBinaryTree(build_tree([1])) == 0
    assert s.diameterOfBinaryTree(None) == 0
    print("6. diameterOfBinaryTree     OK")


    # 8. Subtree
    root = build_tree([3, 4, 5, 1, 2])
    assert s.isSubtree(root, build_tree([4, 1, 2])) is True
    root2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    assert s.isSubtree(root2, build_tree([4, 1, 2])) is False
    print("8. isSubtree                OK")


    # 11. Valid BST
    assert s.isValidBST(build_tree([2, 1, 3])) is True
    assert s.isValidBST(build_tree([1, 2, 3])) is False
    assert s.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])) is False
    assert s.isValidBST(build_tree([5, 4, 6, None, None, 3, 7])) is False
    print("11. isValidBST              OK") '''

    print("\nAll tests passed.") 


if __name__ == "__main__":
    run_tests()