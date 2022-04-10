class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        i, a = 0, strs[0]
        for i in range(len(a)):
            for b in strs:
                if i >= len(b) or a[i] != b[i]: return a[:i]
            i += 1
        return a[:i]
