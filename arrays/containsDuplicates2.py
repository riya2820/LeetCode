from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        # edge case: no unique value in list
        if len(nums) == len(set(nums)):
            return False

        d = defaultdict(list)
        for idx, num in enumerate(nums):
            if num in d.keys():
                d[num].append(idx)
            else:
                d[num] = [idx]


        diff = 1000
        for key, val in d.items():
            val.sort()
            for i in range(len(val)-1):
                if abs(val[i+1]-val[i]) < diff:
                    diff = abs(val[i+1]-val[i])

        return diff <= k


# Test Case 1
nums = [1,2,3,1]
k = 3

# Test Case 2
nums2 = [1,0,1,1]
k2 = 1

# Test Case 3 
nums3 = [1,2,3,1,2,3] # -> False 
k3 = 2

# nums[i] == nums[j] and abs(i - j) <= k.
A = Solution()
print(A.containsNearbyDuplicate(nums,k))
# print(A.containsNearbyDuplicate(nums2,k2))
# print(A.containsNearbyDuplicate(nums3,k3))