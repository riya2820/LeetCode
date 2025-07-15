from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        result = []
        
        for num in nums:
            d[num] += 1
            
        d = {k: v for k, v in sorted(d.items(), key=lambda k: (k[1],-k[0]))}
        print(d)  
        
        for k, v in d.items():
            while v >= 1:
                result.append(k)
                v -= 1
                
        return result
