class Solution:
    def arrayPairSum(self, nums):
        result = 0
        i = 0
        nums.sort()

        for i in range(0,len(nums), 2): 
            result += nums[i]

        return result


# O(N) time complexity 
nums = [1,2,3,4]
A = Solution()
print(A.arrayPairSum(nums))