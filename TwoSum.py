class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            remaining = target - val
            if remaining in d:
                return [d[remaining], i]
            d[val] = i
        return []
            
