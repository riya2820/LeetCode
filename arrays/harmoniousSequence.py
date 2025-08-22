from collections import defaultdict

class Solution:
    def findLHS(self, nums):
        max_length = 0
        d = defaultdict(int)

        for num in nums:
            d[num] += 1 # or could use counter 

        for num in d:
            if num+1 in d:
                current_length = d[num] + d[num+1]
                max_length = max(max_length, current_length)

        return max_length


A = Solution()
nums = [1,3,2,2,5,2,3,7]
print(A.findLHS(nums))

# O(N) time
# O(N) space 
