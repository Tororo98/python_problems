def isPalindrome(x):
    # Declaration of variables for the problem
    if x < 0:
        return False
    
    digits = []
    # Extract digits from the number
    while x > 0:
        digits.append(x % 10)
        x //= 10

    # Check if the number is a palindrome
    return digits == digits[::-1]

if __name__ == "__main__":
    # Test the function
    print(isPalindrome(121))  # Output: True
    print(isPalindrome(-121))  # Output: False
    print(isPalindrome(10))  # Output: False

def checkPalindromeUsingStr(x):
    # Check if the number is a palindrome
    return str(x) == str(x)[::-1]