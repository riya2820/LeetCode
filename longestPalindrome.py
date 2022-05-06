def longestPalindrome(s):
    #O(N) best case time complexity with O(N^2) worst case
    if len(s) <= 1: #edge case
        return s

    res = []

    for idx in range(len(s)):
        # Check for odd length palindrome with idx at its center
        left = right = idx
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(res):
                res = s[left:right + 1]
            left -= 1
            right += 1

        # Check for even length palindrome with idx and idx-1 as its center
        left = idx - 1
        right = idx
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(res):
                res = s[left:right + 1]
            left -= 1
            right += 1

    return res
    
print(longestPalindrome("babad"))
