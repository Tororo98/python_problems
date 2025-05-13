def fizzBuzz(n: int) -> str:
    """
    Returns 'Fizz' if n is divisible by 3, 'Buzz' if n is divisible by 5,
    'FizzBuzz' if n is divisible by both, and the number itself otherwise.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
    
if __name__ == "__main__":
    # Test the function
    for i in range(1, 16):
        print(fizzBuzz(i))
    # Output:
    # 1
    # 2
    # Fizz
    # 4
    # Buzz
    # Fizz
    # 7
    # 8
    # Fizz
    # Buzz
    # 11
    # Fizz
    # 13
    # 14
    # FizzBuzz