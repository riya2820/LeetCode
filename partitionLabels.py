class Solution:
    def partitionLabels(self, s: str) -> List[int]:
    # O(N) time
        lastIndex = {}
        result = []
        size, end = 0, 0
        
        for idx, char in enumerate(s):
            lastIndex[char] = idx
            
            
        for idx, char in enumerate(s):
            size += 1
            if lastIndex[char] > end:
                # update end 
                end = lastIndex[char]
                
            if idx == end:
                result.append(size)
                size = 0
                
        return result
