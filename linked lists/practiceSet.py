"""
NeetCode 150 — Hashing + Linked Lists  [PRACTICE STUBS]
Single file, runnable offline:  python3 neetcode_linkedlists_practice.py

Fill in each method. Tests at the bottom check your work — run the file to
see which pass. An unimplemented method raises; the suite stops there.

Problems:
  1. Design HashSet
  2. Design HashMap
  3. Reverse a Linked List
  4. Merge Two Sorted Linked Lists
  5. Linked List Cycle Detection
  6. Palindrome Linked List
  7. Remove Linked List Elements
  8. Middle of the Linked List
  9. Intersection of Two Linked Lists
"""

from typing import Optional


# ----------------------------------------------------------------------
# Scaffolding — ListNode + helpers. Don't reimplement these; use them in
# your own scratch tests. (build_list / to_list / make_cycle / intersect)
# ----------------------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(vals) -> Optional[ListNode]:
    """Python list -> linked list. [] -> None."""
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list:
    """Linked list -> Python list. (Don't call on a cyclic list.)"""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def make_cycle(vals, pos) -> Optional[ListNode]:
    """Build a list; connect the tail's next to the node at index `pos`.
    pos = -1 means no cycle."""
    head = build_list(vals)
    if not head:
        return None
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return head


def make_intersection(a_only, b_only, shared):
    """Build two lists that share a common tail.
    Returns (headA, headB, intersection_node). Shared can be [] (-> None)."""
    shared_head = build_list(shared)

    def append_tail(head, tail):
        if not head:
            return tail
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = tail
        return head

    headA = append_tail(build_list(a_only), shared_head)
    headB = append_tail(build_list(b_only), shared_head)
    return headA, headB, shared_head


# ----------------------------------------------------------------------
# 1. Design HashSet
# HINT: build it yourself — don't wrap Python's set(). Use a fixed array of
#       buckets (size e.g. 1000) and chaining: bucket index = key % size,
#       each bucket is a list. add/remove/contains walk the bucket's list.
# ----------------------------------------------------------------------
class MyHashSet:
    def __init__(self):
        raise NotImplementedError

    def add(self, key: int) -> None:
        raise NotImplementedError

    def remove(self, key: int) -> None:
        raise NotImplementedError

    def contains(self, key: int) -> bool:
        raise NotImplementedError


# ----------------------------------------------------------------------
# 2. Design HashMap
# HINT: same bucket/chaining idea as HashSet, but store (key, value) pairs.
#       put overwrites if key exists; get returns -1 if absent; remove drops
#       the pair. Each bucket holds a list of [key, value].
# ----------------------------------------------------------------------
class MyHashMap:
    def __init__(self):
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def remove(self, key: int) -> None:
        raise NotImplementedError


class Solution:
    # ------------------------------------------------------------------
    # 3. Reverse a Linked List
    # HINT: walk with prev=None, cur=head. Each step: save cur.next, point
    #       cur.next back to prev, advance prev and cur. Return prev.
    # ------------------------------------------------------------------
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []

        curr = head
        prev = None
        # p,     c
        #    1 -> 2 -> 3 -> 4
        while curr and curr.next:
            prev = curr.next
            prev.next = curr

        return prev

    # ------------------------------------------------------------------
    # 4. Merge Two Sorted Linked Lists
    # HINT: dummy head + tail pointer. Compare list1/list2 heads, attach the
    #       smaller, advance it. Attach whatever's left at the end.
    # ------------------------------------------------------------------
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 3- > 7
        # 2 -> 4 -> 6 

        # 1 
        merged = ListNode(-1)
        prev = merged
        # merged = ListNode(-1) # dummy node

        while list1.val and list2.val:
            if list1.val < list2.val:
                prev.next = list1.val
                list1 = list1.next
            else:
                prev.next = list2.val
                list2 = list2.next
            
        if list1:
            merged.next = list1
        if list2:
            merged.next = list2

        return merged

    # ------------------------------------------------------------------
    # 5. Linked List Cycle Detection
    # HINT: Floyd's — slow moves 1, fast moves 2. If they ever meet there's
    #       a cycle; if fast hits None, there isn't.
    # ------------------------------------------------------------------
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while head.next.next:
            slow = head.next
            fast = head.next.next
            if slow == fast:
                return True     

        return False

    # ------------------------------------------------------------------
    # 6. Palindrome Linked List
    # HINT: find middle (slow/fast), reverse the second half, then compare
    #       the two halves node by node. (Or dump values to a list and use
    #       two pointers — simpler but O(n) space.)
    # ------------------------------------------------------------------
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        raise NotImplementedError

    # ------------------------------------------------------------------
    # 7. Remove Linked List Elements
    # HINT: dummy node before head handles removals at the front. Walk with
    #       a prev pointer; when cur.val == val, splice it out (prev.next =
    #       cur.next). Return dummy.next.
    # ------------------------------------------------------------------
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return 

        prev = None 
        curr = head

        while curr.next:
            prev = curr
            if curr.val == val:
                curr.next = curr.next.next
            curr = curr.next

        return head

    # ------------------------------------------------------------------
    # 8. Middle of the Linked List  (if even count, return the SECOND middle)
    # HINT: slow/fast pointers; when fast reaches the end, slow is at middle.
    # ------------------------------------------------------------------
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise NotImplementedError

    # ------------------------------------------------------------------
    # 9. Intersection of Two Linked Lists  (return the shared NODE, not value)
    # HINT: two pointers a, b. When one hits None, redirect it to the OTHER
    #       list's head. They meet at the intersection after at most len(a)+
    #       len(b) steps (or both reach None if no intersection).
    # ------------------------------------------------------------------
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        raise NotImplementedError


# ----------------------------------------------------------------------
# Tests — encode the expected answers, so they double as the spec.
# ----------------------------------------------------------------------
def run_tests():
    s = Solution() 

    # 3. Reverse
    print(to_list(s.reverseList(build_list([1, 2, 3, 4, 5])))) # == [5, 4, 3, 2, 1]
    print(to_list(s.reverseList(build_list([])))) # == []
    print(to_list(s.reverseList(build_list([1])))) # == [1]
    print("3. reverseList              OK")

    # 4. Merge Two Sorted Lists
    assert to_list(s.mergeTwoLists(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(s.mergeTwoLists(build_list([]), build_list([]))) == []
    assert to_list(s.mergeTwoLists(build_list([]), build_list([0]))) == [0]
    print("4. mergeTwoLists            OK")

    # 5. Cycle Detection
    assert s.hasCycle(make_cycle([3, 2, 0, -4], 1)) is True
    assert s.hasCycle(make_cycle([1, 2], 0)) is True
    assert s.hasCycle(make_cycle([1], -1)) is False
    assert s.hasCycle(build_list([])) is False
    print("5. hasCycle                 OK")

    '''
    # 1. Design HashSet
    hs = MyHashSet()
    hs.add(1)
    hs.add(2)
    assert hs.contains(1) is True
    assert hs.contains(3) is False
    hs.add(2)
    hs.remove(2)
    assert hs.contains(2) is False
    assert hs.contains(1) is True
    print("1. MyHashSet                OK")

    # 2. Design HashMap
    hm = MyHashMap()
    hm.put(1, 1)
    hm.put(2, 2)
    assert hm.get(1) == 1
    assert hm.get(3) == -1
    hm.put(2, 1)            # overwrite
    assert hm.get(2) == 1
    hm.remove(2)
    assert hm.get(2) == -1
    print("2. MyHashMap                OK"


    s = Solution() 

    # 3. Reverse
    assert to_list(s.reverseList(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(s.reverseList(build_list([]))) == []
    assert to_list(s.reverseList(build_list([1]))) == [1]
    print("3. reverseList              OK")

    # 4. Merge Two Sorted Lists
    assert to_list(s.mergeTwoLists(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(s.mergeTwoLists(build_list([]), build_list([]))) == []
    assert to_list(s.mergeTwoLists(build_list([]), build_list([0]))) == [0]
    print("4. mergeTwoLists            OK")

    # 5. Cycle Detection
    assert s.hasCycle(make_cycle([3, 2, 0, -4], 1)) is True
    assert s.hasCycle(make_cycle([1, 2], 0)) is True
    assert s.hasCycle(make_cycle([1], -1)) is False
    assert s.hasCycle(build_list([])) is False
    print("5. hasCycle                 OK")

    # 6. Palindrome
    assert s.isPalindrome(build_list([1, 2, 2, 1])) is True
    assert s.isPalindrome(build_list([1, 2, 3, 2, 1])) is True
    assert s.isPalindrome(build_list([1, 2, 3])) is False
    assert s.isPalindrome(build_list([1])) is True
    print("6. isPalindrome             OK")

    # 7. Remove Elements
    assert to_list(s.removeElements(build_list([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert to_list(s.removeElements(build_list([7, 7, 7, 7]), 7)) == []
    assert to_list(s.removeElements(build_list([]), 1)) == []
    print("7. removeElements           OK")

    # 8. Middle (even count -> second middle)
    assert to_list(s.middleNode(build_list([1, 2, 3, 4, 5]))) == [3, 4, 5]
    assert to_list(s.middleNode(build_list([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]
    assert to_list(s.middleNode(build_list([1]))) == [1]
    print("8. middleNode               OK")

    # 9. Intersection
    headA, headB, inter = make_intersection([4, 1], [5, 6, 1], [8, 4, 5])
    assert s.getIntersectionNode(headA, headB) is inter
    headA2, headB2, _ = make_intersection([2, 6, 4], [1, 5], [])  # no shared tail
    assert s.getIntersectionNode(headA2, headB2) is None
    print("9. getIntersectionNode      OK")
    '''

    print("\nAll tests passed.")


if __name__ == "__main__":
    run_tests()