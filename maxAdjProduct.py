def find_maximum_adjacent_product(input_list):
    """
    Finds the largest product between any 2 adjacent elements in a list if no 2 adjacent elements exists returns -inf
    Example:
        find_maximum_adjacent_product([3, 6, -2, -5, 7, 3])
        >>> 21
        find_maximum_adjacent_product([3])
        >>> -inf
    :param input_list: list
    :return: float
    """
    if len(input_list) < 2:
        return float('-inf')

    maximum = float('-inf')
    for idx, element in enumerate(input_list):
        try:
            candidate = element * input_list[idx + 1]
        except IndexError:
            candidate = float('-inf')

        if candidate>=maximum:
            maximum = candidate

    return maximum

input_list = [3, 6, -2, -5, 7, 3]
print(find_maximum_adjacent_product(input_list))