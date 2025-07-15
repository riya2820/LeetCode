class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i, n in enumerate(nums): 
            nums[i] = -n
        heapify(nums)

        while nums and k > 1: # 1
            n1 = -heappop(nums) # remove largest element  # [3,2,1,5,4]
            k -= 1 

        return -heappop(nums) # return the largest element left in heap # 5
