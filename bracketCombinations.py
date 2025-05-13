def bracketCombinations(n):
    """
    Generate all combinations of n pairs of parentheses.
    
    :param n: Number of pairs of parentheses
    :return: List of valid combinations
    """
    def generate(p, left, right):
        if left == 0 and right == 0:
            result.append(p)
            return
        if left > 0:
            generate(p + '(', left - 1, right)
        if right > left:
            generate(p + ')', left, right - 1)

    result = []
    generate('', n, n)
    return result

if __name__ == "__main__":
    # Test the function
    n = 2
    combinations = bracketCombinations(n)
    print(f"All combinations of {n} pairs of parentheses:")
    for combo in combinations:
        print(combo)
    print(len(combinations))  # Output: 5