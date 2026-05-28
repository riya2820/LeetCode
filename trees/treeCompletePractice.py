"""
LeetCode 783: Minimum Distance Between BST Nodes
Practice file with three in-order traversal styles.

Run directly: `python min_diff_bst_practice.py`
"""

from typing import Optional, List, Iterator


# ----------------------------------------------------------------------
# TreeNode (standard LeetCode definition)
# ----------------------------------------------------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ----------------------------------------------------------------------
# Solution
# ----------------------------------------------------------------------

class Solution:

    # ------------- In-order traversal: three flavors -------------

    def inorder_recursive(self, root: Optional[TreeNode]) -> List[int]:
        """Returns in-order traversal as a list, using recursion."""
        result = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)
        helper(root)
        return result

    def inorder_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """Returns in-order traversal as a list, using an explicit stack."""
        result = []
        stack = []
        node = root
        while node or stack:
            while node:                 # go as far left as possible
                stack.append(node)
                node = node.left
            node = stack.pop()          # backtrack to most recent unvisited
            result.append(node.val)     # visit
            node = node.right           # then pivot right
        return result

    def inorder_generator(self, root: Optional[TreeNode]) -> Iterator[int]:
        """Yields in-order values lazily. Great for early-exit problems."""
        if not root:
            return
        yield from self.inorder_generator(root.left)
        yield root.val
        yield from self.inorder_generator(root.right)

    # ------------- minDiffInBST: three implementations -------------

    def minDiffInBST_recursive(self, root: Optional[TreeNode]) -> int:
        """Recursive in-order with `self.prev` as instance state."""
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.min_diff

    def minDiffInBST_iterative(self, root: Optional[TreeNode]) -> int:
        """Iterative in-order with an explicit stack. No recursion."""
        stack = []
        node = root
        prev = None
        min_diff = float('inf')
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            node = node.right
        return min_diff

    def minDiffInBST_generator(self, root: Optional[TreeNode]) -> int:
        """Treats the traversal as a stream — cleanest version."""
        prev = None
        min_diff = float('inf')
        for val in self.inorder_generator(root):
            if prev is not None:
                min_diff = min(min_diff, val - prev)
            prev = val
        return min_diff


# ----------------------------------------------------------------------
# Helper: build a tree from a level-order list (LeetCode style)
# ----------------------------------------------------------------------

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from level-order values; use None for missing nodes.

    Example: [4, 2, 6, 1, 3] →
              4
             / \
            2   6
           / \
          1   3
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ----------------------------------------------------------------------
# Test cases
# ----------------------------------------------------------------------

def run_tests():
    sol = Solution()

    # ---- in-order traversal ----
    print("=" * 64)
    print("IN-ORDER TRAVERSAL")
    print("=" * 64)

    inorder_cases = [
        # (description, level_order_input, expected_inorder)
        ("Empty tree",                  [],                                                 []),
        ("Single node",                 [5],                                                [5]),
        ("Balanced BST",                [5, 3, 8, 1, 4, 7, 10],                             [1, 3, 4, 5, 7, 8, 10]),
        ("Right-skewed",                [1, None, 5, None, 10],                             [1, 5, 10]),
        ("Left-skewed",                 [4, 3, None, 2, None, 1],                           [1, 2, 3, 4]),
        ("Widget tree (5,3,8,_,4,_,10)", [5, 3, 8, None, 4, None, 10],                      [3, 4, 5, 8, 10]),
        ("Grandparent tree",            [8, 3, 12, 1, 6, None, 14, None, None, 4],          [1, 3, 4, 6, 8, 12, 14]),
    ]

    passed = failed = 0
    for desc, vals, expected in inorder_cases:
        root = build_tree(vals)
        rec = sol.inorder_recursive(root)
        itr = sol.inorder_iterative(root)
        gen = list(sol.inorder_generator(root))
        ok = rec == expected and itr == expected and gen == expected
        status = "PASS" if ok else "FAIL"
        passed += ok
        failed += not ok
        print(f"[{status}] {desc}")
        if not ok:
            print(f"        expected = {expected}")
            print(f"        rec      = {rec}")
            print(f"        iter     = {itr}")
            print(f"        gen      = {gen}")

    print(f"\nIn-order: {passed} passed, {failed} failed\n")

    # ---- minDiffInBST ----
    print("=" * 64)
    print("MIN DIFF IN BST")
    print("=" * 64)

    mindiff_cases = [
        # (description, level_order_input, expected_min_diff)
        ("LeetCode ex 1: [4,2,6,1,3]",      [4, 2, 6, 1, 3],                                 1),
        ("LeetCode ex 2: [1,0,48,_,_,12,49]", [1, 0, 48, None, None, 12, 49],               1),
        ("Two nodes",                       [10, 5],                                          5),
        ("Widget tree",                     [5, 3, 8, None, 4, None, 10],                     1),
        ("Grandparent tree",                [8, 3, 12, 1, 6, None, 14, None, None, 4],        1),
        ("Large even gaps",                 [100, 50, 200, 25, 75, 150, 300],                25),
        ("Negative values",                 [0, -5, 10, -10, -2],                             2),
        ("Right-skewed",                    [1, None, 5, None, 10],                           4),
        ("Min diff at the bottom",          [50, 20, 80, 10, 30, 70, 90, 5, 15],              5),
    ]

    passed = failed = 0
    for desc, vals, expected in mindiff_cases:
        root = build_tree(vals)
        rec = sol.minDiffInBST_recursive(root)
        itr = sol.minDiffInBST_iterative(root)
        gen = sol.minDiffInBST_generator(root)
        ok = rec == expected and itr == expected and gen == expected
        status = "PASS" if ok else "FAIL"
        passed += ok
        failed += not ok
        print(f"[{status}] {desc}")
        if not ok:
            print(f"        expected = {expected}")
            print(f"        rec / iter / gen = {rec} / {itr} / {gen}")

    print(f"\nminDiffInBST: {passed} passed, {failed} failed")


if __name__ == "__main__":
    run_tests()