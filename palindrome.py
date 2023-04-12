def isPalindrome(x):
    # Declaration of variables for the problem
    flag = False
    digits = []
    revDigits = []

    # store digits in array
    if x>0:
        while(x>0):
            digit,x = x%10, x//10
            digits.append(digit)

        # Reverse digits
        for item in reversed(digits):
            revDigits.append(item)

        # Chekc if number is palindrome or not
        if(revDigits==digits):
            flag = True

    return flag

print(isPalindrome(121))