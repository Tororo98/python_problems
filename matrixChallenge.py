""" 
    This function test wether a sudoku board is valid, assuming is of size 9x9 and the dimensions are correct.
    If not, it will return the incorrect quadrants

    if the condition for false is fulfilled:
        erase the return false
        create a global set for quadrants
        for rows:
            if the row is 1 quadrant could be 1-3, if row is 2 quadrant could be 4-6... and so on
            add the index of wrong ones to the quadrants set
                check if quadrant is not there
        for cols:
            if the col is 1 quadrant could be 1,4,7 and so on
            add the index of wrong ones to the quadrants set
                check if quadrant is not there
        for subgrids, i marks the quadrant
 
"""

A = [
"(1,2,3,4,5,6,7,8,x)",
"(x,x,x,x,x,x,x,x,x)",
"(x,x,x,x,x,x,x,x,x)",
"(x,x,x,2,x,x,x,x,x)",
"(1,x,x,x,x,x,x,x,1)",
"(x,x,x,x,x,x,x,x,x)",
"(x,x,x,x,x,x,x,x,5)",
"(3,x,x,x,x,x,x,x,x)",
"(1,x,x,x,x,x,x,x,x)"
]

def is_valid_sudoku(A):
    #Conver input to valid strings
    strArr = ["".join(row).replace("(", "").replace(")", "").replace(",", "") for row in A]
    wrong_quadrants = set()

    # Check rows and add wrong quadrants
    i_row = 0
    for row in strArr:
        numbers = set()
        actual_col = 0
        for char in row:
            if char != 'x':
                if char in numbers:
                    # Calculate actual quadrant, row check
                    ordered_numbers = list(row)
                    indexs = [i for i, x in enumerate(ordered_numbers) if x == char]
                    quad_index = [get_quadrant_number_optimized(i_row, x) for x in indexs]
                    actual_indexs = [x+1 for x in quad_index]

                    #Add the wrong quadrant
                    if (i_row >= 0 and i_row < 3):
                        if (actual_col >= 0 and actual_col < 3): wrong_quadrants.add(1), wrong_quadrants.update(actual_indexs)

                        if (actual_col >= 3 and actual_col < 6): wrong_quadrants.add(2), wrong_quadrants.update(actual_indexs)

                        if (actual_col >= 6 and actual_col < 9): wrong_quadrants.add(3), wrong_quadrants.update(actual_indexs)
                    if (i_row >= 3 and i_row < 6):
                        if (actual_col >= 0 and actual_col < 3): wrong_quadrants.add(4), wrong_quadrants.update(actual_indexs)

                        if (actual_col >= 3 and actual_col < 6): wrong_quadrants.add(5), wrong_quadrants.update(actual_indexs)

                        if (actual_col >= 6 and actual_col < 9): wrong_quadrants.add(6), wrong_quadrants.update(actual_indexs)
                    if (i_row >= 6 and i_row < 9):
                        if (actual_col >= 0 and actual_col < 3): wrong_quadrants.add(7), wrong_quadrants.update(actual_indexs)

                        if (actual_col >= 3 and actual_col < 6): wrong_quadrants.add(8), wrong_quadrants.update(actual_indexs)

                        if (actual_col >= 6 and actual_col < 9): wrong_quadrants.add(9), wrong_quadrants.update(actual_indexs)
                numbers.add(char)
            actual_col += 1
        i_row += 1

    # Check columns
    for col in range(9):
        numbers = set()
        ordered_numbers = []
        for row in range(9):
            char = strArr[row][col]
            ordered_numbers.append(char)
            if char != 'x':
                if char in numbers:                   
                    actual_indexs = get_quadrants(ordered_numbers)
                    if (col >= 0 and col < 3):
                        if (row >= 0 and row < 3): wrong_quadrants.add(1), wrong_quadrants.update(actual_indexs)
                            
                        if (row >= 3 and row < 6): wrong_quadrants.add(4), wrong_quadrants.update(actual_indexs)
                            
                        if (row >= 6 and row < 9): wrong_quadrants.add(7), wrong_quadrants.update(actual_indexs)
                    if (col >= 3 and col < 6):
                        if (row >= 0 and row < 3): wrong_quadrants.add(2), wrong_quadrants.update(actual_indexs)
                            
                        if (row >= 3 and row < 6): wrong_quadrants.add(5), wrong_quadrants.update(actual_indexs)
                            
                        if (row >= 6 and row < 9): wrong_quadrants.add(8), wrong_quadrants.update(actual_indexs)
                                         
                    if (col >= 6 and col < 9):
                        if (row >= 0 and row < 3): wrong_quadrants.add(3), wrong_quadrants.update(actual_indexs)
                            
                        if (row >= 3 and row < 6): wrong_quadrants.add(6), wrong_quadrants.update(actual_indexs)
                            
                        if (row >= 6 and row < 9): wrong_quadrants.add(9), wrong_quadrants.update(actual_indexs)                                                                               
                numbers.add(char)

    # Check sub-grids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            numbers = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    char = strArr[row][col]
                    if char != 'x':
                        if char in numbers:
                            if (row >= 0 and row < 3):
                                if (col >= 0 and col < 3): wrong_quadrants.add(1)

                                if (col >= 3 and col < 6): wrong_quadrants.add(2)

                                if (col >= 6 and col < 9): wrong_quadrants.add(3)
                            if (row >= 3 and row < 6):
                                if (col >= 0 and col < 3): wrong_quadrants.add(4)

                                if (col >= 3 and col < 6): wrong_quadrants.add(5)

                                if (col >= 6 and col < 9): wrong_quadrants.add(6)
                            if (row >= 6 and row < 9):
                                if (col >= 0 and col < 3): wrong_quadrants.add(7)

                                if (col >= 3 and col < 6): wrong_quadrants.add(8)

                                if (col >= 6 and col < 9): wrong_quadrants.add(9)
                        numbers.add(char)

    # If all checks pass, return True
    return wrong_quadrants

# Get quadrant when iterating by column
def get_quadrants(column):
    quadrants = []
    for i, val in enumerate(column):
        if val != "x":
            row = i % 9
            col = i // 9
            quadrant_row = (row // 3) * 3
            quadrant_col = (col // 3) * 3
            quadrant_num = (quadrant_row // 3) * 3 + (quadrant_col // 3) + 1
            quadrants.append(quadrant_num)
    return quadrants

# Get quadrant when iterating by row
def get_quadrant_number(row, col):
    # Determine which quadrant the current element is in
    if col < 3:
        if row < 3:
            quadrant_number = 0
        elif row < 6 and row >=3:
            quadrant_number = 3
        else:
            quadrant_number = 6
    elif col < 6 and col >=3:
        if row < 3:
            quadrant_number = 1
        elif row < 6 and row >=3:
            quadrant_number = 4
        else:
            quadrant_number = 7
    else:
        if row < 3:
            quadrant_number = 2
        elif row < 6 and row >=3:
            quadrant_number = 5
        else:
            quadrant_number = 8

    return quadrant_number

def get_quadrant_number_optimized(row, col):
    # Determine which quadrant the current element is in
    quadrant_number = (row // 3) * 3 + (col // 3)

    return quadrant_number


def check_valid():
    validation_obj = is_valid_sudoku(A)

    if (len(validation_obj) == 0):
        return "legal"
    else:
        return validation_obj

print(check_valid())