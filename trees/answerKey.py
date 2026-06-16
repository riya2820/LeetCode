"""
NeetCode 150 — Graphs (grids) + Binary Trees
Single file, runnable offline:  python3 neetcode_trees_graphs.py

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
    #    DFS: each unvisited "1" starts a new island, sink the whole island.
    # ------------------------------------------------------------------
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        def sink(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"  # mark visited
            sink(r + 1, c)
            sink(r - 1, c)
            sink(r, c + 1)
            sink(r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    sink(r, c)
        return count

    # ------------------------------------------------------------------
    # 2. Max Area of Island  (grid of 0/1 ints)
    #    DFS returns area of each island, track the max.
    # ------------------------------------------------------------------
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        def area(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 0  # mark visited
            return 1 + area(r + 1, c) + area(r - 1, c) + area(r, c + 1) + area(r, c - 1)

        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    best = max(best, area(r, c))
        return best

    # ------------------------------------------------------------------
    # 3. Rotting Fruit  (0 empty, 1 fresh, 2 rotten)
    #    Multi-source BFS from all rotten cells at once; count minutes.
    #    Return -1 if any fresh fruit can never rot.
    # ------------------------------------------------------------------
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh > 0:
            for _ in range(len(q)):  # process one minute (whole layer)
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1

    # ------------------------------------------------------------------
    # 4. Invert a Binary Tree
    # ------------------------------------------------------------------
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # ------------------------------------------------------------------
    # 5. Max Depth of Binary Tree
    # ------------------------------------------------------------------
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # ------------------------------------------------------------------
    # 6. Binary Tree Diameter  (longest path between any two nodes, in edges)
    #    For each node, depth(left)+depth(right) is a candidate diameter.
    # ------------------------------------------------------------------
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.diameter

    # ------------------------------------------------------------------
    # 7. Same Binary Tree
    # ------------------------------------------------------------------
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # ------------------------------------------------------------------
    # 8. Subtree of a Binary Tree
    #    At each node of root, check isSameTree against subRoot.
    # ------------------------------------------------------------------
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # ------------------------------------------------------------------
    # 9. Level Order Traversal  (BFS, group by level)
    # ------------------------------------------------------------------
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result

    # ------------------------------------------------------------------
    # 10. Right Side View  (last node seen at each BFS level)
    # ------------------------------------------------------------------
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:  # rightmost node of this level
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result

    # ------------------------------------------------------------------
    # 11. Valid Binary Search Tree
    #     Carry (low, high) bounds down the tree.
    # ------------------------------------------------------------------
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float("-inf"), float("inf"))


# ----------------------------------------------------------------------
# Tests — simple asserts. Prints a line per problem, raises on failure.
# ----------------------------------------------------------------------
def run_tests():
    s = Solution()

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

    # 4. Invert Binary Tree
    inverted = s.invertTree(build_tree([1, 2, 3, 4, 5, 6, 7]))
    assert s.levelOrder(inverted) == [[1], [3, 2], [7, 6, 5, 4]]
    assert s.invertTree(None) is None
    print("4. invertTree               OK")

    # 5. Max Depth
    assert s.maxDepth(build_tree([1, 2, 3, None, None, 4])) == 3
    assert s.maxDepth(None) == 0
    assert s.maxDepth(build_tree([1])) == 1
    print("5. maxDepth                 OK")

    # 6. Diameter (in edges)
    assert s.diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])) == 3
    assert s.diameterOfBinaryTree(build_tree([1])) == 0
    assert s.diameterOfBinaryTree(None) == 0
    print("6. diameterOfBinaryTree     OK")

    # 7. Same Tree
    assert s.isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True
    assert s.isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) is False
    assert s.isSameTree(None, None) is True
    print("7. isSameTree               OK")

    # 8. Subtree
    root = build_tree([3, 4, 5, 1, 2])
    assert s.isSubtree(root, build_tree([4, 1, 2])) is True
    root2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    assert s.isSubtree(root2, build_tree([4, 1, 2])) is False
    print("8. isSubtree                OK")

    # 9. Level Order
    assert s.levelOrder(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert s.levelOrder(None) == []
    print("9. levelOrder               OK")

    # 10. Right Side View
    assert s.rightSideView(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert s.rightSideView(build_tree([1, 2, 3, 4])) == [1, 3, 4]
    assert s.rightSideView(None) == []
    print("10. rightSideView           OK")

    # 11. Valid BST
    assert s.isValidBST(build_tree([2, 1, 3])) is True
    assert s.isValidBST(build_tree([1, 2, 3])) is False          # 2 > 1 on left -> invalid
    assert s.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])) is False
    assert s.isValidBST(build_tree([5, 4, 6, None, None, 3, 7])) is False  # 3 in right subtree of 5
    print("11. isValidBST              OK")

    print("\nAll tests passed.")


if __name__ == "__main__":
    run_tests()