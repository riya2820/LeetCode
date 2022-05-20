class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        s1 = "."
        s2 = ":"
        
        if s1 in queryIP:
            lst = queryIP.split(".")
            if (len(lst) != 4):
                return "Neither"
            
            for num in lst:
                if num.isdigit() == False:
                    return "Neither"
                if len(num) > 1 and num[0] == "0":
                    return "Neither"
                if len(num) > 3:
                    return "Neither"
                if int(num) > 255 or int(num) < 0:
                    return "Neither"
            return "IPv4"
        
        
        
        elif s2 in queryIP:
            lst = queryIP.split(":")
            if (len(lst) != 8):
                return "Neither"
            hexdigits = '0123456789abcdefABCDEF'
            
            for num in lst:
                if len(num) == 0 or len(num) > 4:
                    return "Neither"
                if not all( i in hexdigits for i in num):
                    return "Neither"
            return "IPv6"
        
        else:
            return "Neither"

