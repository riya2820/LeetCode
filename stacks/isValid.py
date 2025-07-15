class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:
            if char in mapping: #closing brackers
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
                    
            else: #opening 
                stack.append(char)
                
         #if stack is empty, then it is valid
         return not stack
