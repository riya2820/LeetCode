class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if (s == goal):
            return False
    
        copy_s = s[:]
        
        for i in range(len(copy_s)):
            s = s.replace(copy_s[i], "", 1) #remove from start only 1st occurence 
            s += copy_s[i] #add it at the end
            if (s == goal):         
                return True
        
        

        return False
