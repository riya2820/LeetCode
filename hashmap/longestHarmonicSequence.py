from collections import defaultdict

class Solution:
    def findLHS(self, nums):
        d = defaultdict(list)

        for char, idx in enumerate(nums):
            if char in d.keys():
                d[char].append(idx)
            else:
                d[char] = [idx]
            
        length = 0
    
        for num in nums:
            n2 = num+1
            if n2 in d.keys():
                length = abs(nums.index(num) - max(d[nums+1]))

        return length 
     

# nums = [3,2,2,4,6]
nums = [1,3,2,2,5,2,3,7]
A = Solution()
print(A.findLHS(nums))