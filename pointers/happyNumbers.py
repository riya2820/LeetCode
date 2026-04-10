class Solution:
    def isHappy(self, n: int) -> bool:
        nums = list(str(n))
        print(nums)
        i = 0
        total = 10 

        if len(nums) == 0 or len(nums) == 1:
            return False

        while total > 9: 
            print(nums, total)
            nums = list(str(total)) # [8,2]
            total = 0
            while i < len(nums): # [1, 9]
                total += int(nums[i])*int(nums[i]) # 1^2 + 9^9 = 82
                print("-->", nums, total)
                

        return total == 1

A = Solution()
n = 19
print(A.isHappy(n))