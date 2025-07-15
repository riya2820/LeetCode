class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        #Method 1
        #return len(set(sentence)) == 26
        
        #Method 2
        alphabets="abcdefghijklmnopqrstuvwxyz"
        flag=False
        for letter in alphabets:
            if letter not in sentence:
                return False
        return True
