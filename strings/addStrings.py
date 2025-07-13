 def addStrings(self, num1: str, num2: str) -> str:
        # num1 = "11" and num2 = "123" --> 134
        # num1 = "456" and num2 = "77" --> 533 # need to account for carry 
        p1, p2 = len(num1)-1, len(num2)-1
        carry = 0
        result = ""

        while p1 >= 0 and p2 >= 0 or carry:
            digit1 = int(num1[p1]) if p1 >=0 else 0
            digit2 = int(num2[p2]) if p2 >=0 else 0
            # print(digit1, digit2, "\n")
            
            total = digit1 + digit2 + carry 
            result += str(total%10)
            carry = total//10
            # print(total, result, carry, "\n")

            p1 -= 1
            p2 -= 1

        return result[::-1]