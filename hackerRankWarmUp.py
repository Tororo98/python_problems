from itertools import combinations
from datetime import datetime

def min_max_combinations(arr):
    if len(arr) != 5:
        raise ValueError("The input array must contain exactly 5 positive integers.")
    
    # Generate all combinations of 4 elements
    sums = [sum(comb) for comb in combinations(arr, 4)]
    
    # Find the minimum and maximum sums
    min_sum = min(sums)
    max_sum = max(sums)
    
    return min_sum, max_sum

def count_max_repetitions(arr):
    if not arr:
        raise ValueError("The input array must not be empty.")
    
    max_value = max(arr)
    count = arr.count(max_value)
    
    return count


def convert_to_military_time(time_str):
    """
    Convert a 12-hour clock format time string with seconds to military (24-hour) format.
    
    Args:
        time_str (str): Time in 12-hour format with seconds (e.g., "12:01:00PM").
    
    Returns:
        str: Time in 24-hour format with seconds (e.g., "12:01:00").
    """
    
    # Parse the input time string and convert to 24-hour format
    military_time = datetime.strptime(time_str, "%I:%M:%S%p").strftime("%H:%M:%S")
    
    return military_time


# Example usage
if __name__ == "__main__":
    # Test the function with a sample input
    arr = [1, 2, 3, 4, 5]
    min_sum, max_sum = min_max_combinations(arr)
    print(f"Minimum sum: {min_sum}")
    print(f"Maximum sum: {max_sum}")