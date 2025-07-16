class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        result = 0

        for num in nums:
            if num == 1:
                count += 1
                result = max(count, result)
            else:
                count = 0 # reset counter

        return result

# Test Cases
nums1 = [1,1,0,1,1,1]
nums2 = [1,0,1,1,0,1]
nums3 = [0,0]

A = Solution()
print(A.findMaxConsecutiveOnes(nums1))
print(A.findMaxConsecutiveOnes(nums2))
print(A.findMaxConsecutiveOnes(nums3))