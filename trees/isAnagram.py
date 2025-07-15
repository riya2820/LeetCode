class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #return (sorted(s) == sorted(t))
        smap = {} 
        tmap = {}

        for elem in s:
            if elem in smap:
                smap[elem] += 1
            else:
                smap[elem] = 1

        for elem in t:
            if elem in tmap:
                tmap[elem] += 1
            else:
                tmap[elem] = 1
                
        return smap == tmap 
        
            
        
