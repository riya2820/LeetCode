from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = defaultdict(int)
        result = []

        for char in arr:
            d[char] += 1

        for key,val in d.items():
            if val == 1:
                result.append(key)
      
        if k <= len(result):
            return result[k-1]
        else:
            return ""



arr = ["d","b","c","b","c","a"]
k = 2

A = Solution()
print(A.kthDistinct(arr, k))

# O(n) time and O(n) space