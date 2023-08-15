class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return '11' not in bin(n) and '00' not in bin(n)
