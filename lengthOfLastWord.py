class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_s = s.strip().split(" ")[-1] 
        return len(str_s)
