class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = bin(n)[2:]
        result = "0b"
        
        for i in num:
            if i == "0":
                result += "1"
            else:
                result += "0"
       
        return int(result, 2)
 
            
