def isPalindrome(x):
    flag = False
    digits = []
    if x>0:
        while(x>0):
            digit,x = x%10, x//10
            digits.append(digit)

        if(digits.reverse()==digits):
            flag = True
    else:
        return flag
    return flag

print(isPalindrome(121))