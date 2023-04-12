def isPalindrome(x):
    flag = False
    digits = []
    revDigits = []
    if x>0:
        while(x>0):
            digit,x = x%10, x//10
            digits.append(digit)
        for item in reversed(digits):
            revDigits.append(item)
        if(revDigits==digits):
            flag = True
    else:
        return flag
    return flag

print(isPalindrome(123))