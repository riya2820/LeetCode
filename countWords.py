class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = defaultdict(int) 
        count = 0

        for word in words1:
            d1[word] += 1

        for word in words2:
            if word in d1.keys() and d1[word] == 1 and words2.count(word) == 1:
                count += 1
            
        return count 
