class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {"2":"abc",
             "3":"def",
             "4":"ghi",
             "5":"jkl",
             "6":"mno",
             "7":"pqrs",
             "8":"tuv",
             "9":"wxyz"}
        
 
        result = []
        chars = [d[digit] for digit in digits]
        print(chars)
        combs = product(*chars) 
        #print(combs)
        
        for comb in combs:
            print(comb)
            if not comb:
                continue
            string = ''.join(comb)
            result.append(string)
            
        return result
