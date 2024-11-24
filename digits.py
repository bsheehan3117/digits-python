'''
    CS5001
    Spring 2023
    HW2

    Brendan Sheehan

    This is a function to determine the digit in a speficied numer at a
    specified place
'''

'''
    Examples:
    Input: (123456, 1) Output: 6
    Input: (123456, 2) Output: 5
    Input: (123456, 3) Output: 4
    Input: (789123, 4) Output: 9
    Input: (987654, 5) Output: 8
    Input: (246810, 6) Output: 2
    Input: (456, 4) Output: 0
'''


def digit_of_number(number, place):
    
    '''Function: digit_of_number
    Determine the digit in the specified number at the specified place
    Parameters:
    number whose digit is to be determined
    place at which the returned digit is in the given number
    Returns: the digit in the specified number at the specified place
    Require: number is non-negative, place is positive
    Ensure: function returns 0 if the place argument is more than
    the number of digits specified in the number
    '''
    digit = number // (10 ** (place - 1)) % 10
    return (digit)
