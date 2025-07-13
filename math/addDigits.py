def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    digit = 0
    while num > 0:
        digit += num % 10
        num = num//10
        
        if num == 0 and digit > 9:
            num = digit
            digit = 0
            
    return digit
