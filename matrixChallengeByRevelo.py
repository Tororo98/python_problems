# Matrix challenge by Revelo - Solution 1
# Given str array like in examples inside main where each elem is a row and the len of each elem
# represents the columns,
# check wether there is any 2x2 square full of vowels and return its top-left coordinate.
# if multiple return the most top-left, otherwise return not found.


vowels = {"a", "e", "i", "o", "u"}

def convert_to_matrix(strMatrix):
    m = len(strMatrix[0]) #columns
    return [[row[i] for i in range(m)] for row in strMatrix]
    
def is_vowel_square(strMatrix, row, column, vowels):
    return (strMatrix[row][column] in vowels and strMatrix[row][column+1] in vowels and strMatrix[row+1][column] in vowels and strMatrix[row+1][column+1] in vowels)

# Example usage:
def main():
    strMatrix = ["aqrst", "ukaei", "ffooo"]
    strMatrix2 = ["abcd", "eikr", "oufj"]
    strMatrix3 = ["gg", "ff"]
    strMatrix4 = ["aqrst", "ukeio", "ffahu"]
    matrix = convert_to_matrix(strMatrix)
    print(matrix)
    possibleAnswers = []
    m = len(matrix[0]) #columns
    n = len(matrix) #rows
    
    for row in range(n-1):
        for col in range(m-1):
            if is_vowel_square(matrix, row, col, vowels):
                if len(possibleAnswers) > 0:
                    if row <= possibleAnswers[0] and col < possibleAnswers[1]:
                        possibleAnswers[0] = row
                        possibleAnswers[1] = col
                else:
                    possibleAnswers.append(row)
                    possibleAnswers.append(col)
                    
    if len(possibleAnswers) > 0:
        print(possibleAnswers[0], "-", possibleAnswers[1])
    else:
        print("not found")

main()