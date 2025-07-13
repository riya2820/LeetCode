class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        letters={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
        last_amount = letters["M"]
        
        while len(s) > 0:
            if letters[s[0]] > last_amount:
                sum -= 2 * last_amount
            
            sum += letters[s[0]]
            last_amount = letters[s[0]]
            
            s = s[1::]
            
        return sum
