class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:   
        # Alternate way 
        k %= sum(chalk) # skips to last iteration!
        # O(N)
        for i in range(len(chalk)):
            if k - chalk[i] < 0:
                return i
         
            k -= chalk[i]  
