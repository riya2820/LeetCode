class Solution:
    def reverse(self, x: int) -> int:
        a = -pow(2,31)
        b = pow(2,31) -1
        rev = ""
        if x >= b or x <= a:
            return 0
        else:
            s = str(x)
            rev += s[::-1]
            if x < 0:
                if -int(rev[:-1]) >= b or -int(rev[:-1]) <=a:
                    return 0
                else:
                    return -int(rev[:-1])
            else:
                if int(rev) >= b or int(rev) <=a:
                    return 0
                else:
                    return int(rev)
