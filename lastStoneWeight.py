class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # O(logN) time 
        # using maxHeap so negating values ! -> minHeap with negated values 
        for i, s in enumerate(stones):
            stones[i] = -s
        heapify(stones)  
       
        while stones:
            s1 = -heappop(stones)  # the heaviest stone
            if not stones:  # s1 is the remaining stone i.e last element found !
                return s1
            
            s2 = -heappop(stones)  # the second-heaviest stone; s2 <= s1
            
            if s1 > s2:
                heappush(stones, s2-s1)  # push the NEGATED value of s1-s2; i.e., s2-s1
            # else s1 == s2; both stones are destroyed
        
        return 0  # if no more stones remain
