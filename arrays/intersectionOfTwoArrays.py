from collections import defaultdict 

class Solution:
    def intersect(self, nums1, nums2):
        i = 0
        j = 0
        result = []

        nums1.sort()
        nums2.sort()

        while i < len(nums1) and j < len(nums2): # [4,5,9] and [4,4,8,9,9]
            if nums1[i] == nums2[j]:
                # print("match found!", nums1[i], nums2[j])
                # print("pointers",i,j)
                result.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                # print(nums1[i], nums2[j])
                # print("pointers", i, j)
                i += 1

            else:
                j += 1

        return result 

# Test cases
nums1 = [1,2,2,1]
nums2 = [2,2] # [2,2]

nums3 = [4,9,5] # compairng sorted arrays [4,5,9] and [4,4,8,9,9]
nums4 = [9,4,9,8,4] # [4,9] or [9,4]

nums5 = [4,9,5]
nums6 = [9,4,8,4]

A = Solution()
print(A.intersect(nums1, nums2))
print(A.intersect(nums3, nums4)) 
print(A.intersect(nums5, nums6)) 
