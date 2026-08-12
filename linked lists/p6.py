from collections import defaultdict, Counter, deque
# ---------------------------------------------------------------------------
# T1 — Two-sum (hash map). Return indices of the two nums that add to target.
# O(n) time, O(n) space. Warm-up they may open with.
# ---------------------------------------------------------------------------
def two_sum(nums, target):
    # two_sum([2, 7, 11, 15], 9) == [0, 1]
    # 9 -2 = 7 
    # value: index
    d = {}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [d[target-nums[i]], i]
        d[nums[i]] = i

    return None


# ---------------------------------------------------------------------------
# T2 — Group anagrams. Bucket words by sorted-letter signature.
# O(n * k log k). Tests dict-of-lists + a good key choice.
# ---------------------------------------------------------------------------
def group_anagrams(words):
    pass


# ---------------------------------------------------------------------------
# T3 — Merge overlapping intervals. Sort, then sweep.
# Common "did you sort first / handle touching edges" check.
# ---------------------------------------------------------------------------
def merge_intervals(intervals):
    passs


# ---------------------------------------------------------------------------
# T4 — Top-K frequent elements. Counter + heap (or sort).
# Talk trade-off: sort O(n log n) vs heap O(n log k).
# ---------------------------------------------------------------------------
import heapq
def top_k_frequent(nums, k):
    pass


# ---------------------------------------------------------------------------
# T5 — Valid parentheses. Classic stack problem.
# ---------------------------------------------------------------------------
def valid_parens(s):
    pass


# ---------------------------------------------------------------------------
# T6 — First non-repeating character; return its index, else -1.
# Two-pass with a count map. Tests you keep order.
# ---------------------------------------------------------------------------
def first_unique_char(s):
    pass


# ---------------------------------------------------------------------------
# T7 — BFS shortest path length in an unweighted graph (adjacency dict).
# Slightly harder; shows you know BFS vs DFS for shortest path.
# ---------------------------------------------------------------------------
def shortest_path_len(graph, start, goal):
    pass                            


# ===========================================================================
# TESTS
# ===========================================================================
def _run():
    print(two_sum([2, 7, 11, 15], 9))
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([1, 2], 10) is None
    print("Passed 1")

    ga = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(g) for g in ga) == sorted(
        sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

    assert merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]) == [
        (1, 6), (8, 10), (15, 18)]
    assert merge_intervals([(1, 4), (4, 5)]) == [(1, 5)]
    assert merge_intervals([]) == []

    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

    assert valid_parens("()[]{}") is True
    assert valid_parens("(]") is False
    assert valid_parens("([)]") is False
    assert valid_parens("{[]}") is True

    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1

    g = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"]}
    assert shortest_path_len(g, "a", "e") == 3
    assert shortest_path_len(g, "a", "a") == 0
    assert shortest_path_len(g, "e", "a") == -1

    print("All tests passed ✅")

if __name__ == "__main__":
    _run()