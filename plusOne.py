class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        for i in range(len(digits)):
            index = n-1-i
            
            if digits[index] == 9: #if 9 then carry 1
                digits[index] = 0
            else:
                digits[index] += 1 #last digit + 1
                return digits 
        return [1] + digits  #edge case: all numbers are 9
       #returns [1,0..] since last digit was 9
            
