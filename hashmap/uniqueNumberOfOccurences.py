from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr):
        d = defaultdict(int)

        for num in arr:
            d[num] += 1

        return len(list(d.values())) == len(set(d.values()))


# Test Cases
# arr = [1,2,2,1,1,3]
arr = [1,2]
A = Solution()
print(A.uniqueOccurrences(arr))
        
# O(n) time and O(n) space 