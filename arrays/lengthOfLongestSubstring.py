class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            result = max(result, j - i + 1)
            mp[s[j]] = j + 1

        return result
