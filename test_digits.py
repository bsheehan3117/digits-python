'''
    CS5001
    Spring 2023
    HW2

    Brendan Sheehan

    This program tests the digits function
'''

from digits import digit_of_number

def test_digit(number, place, expected):
    
    '''Function test_digit

    Parameters:
    Number whose digit is to be determined
    Place at which the returned digit is in the given number
    Return: nothing, print inputs & actual vs expected.

    Examples:
    Input: (123456, 1) Output: 6
    Input: (123456, 2) Output: 5
    Input: (123456, 3) Output: 4
    Input: (789123, 4) Output: 9
    Input: (987654, 5) Output: 8
    Input: (246810, 6) Output: 2
    Input: (456, 4) Output: 0
    '''
    print("For number", number, "Finding digit at place", place)
    actual = digit_of_number(number, place)
    print("\tExpected = ", expected)
    print("\tResult = ", actual)

def main():
        
        # test 1
        test_digit(123456, 1, 6)

        # test 2
        test_digit(123456, 2, 5)

        # test 3
        test_digit(123456, 3, 4)

        # test 4
        test_digit(789123, 4, 9)

        # test 5
        test_digit(987654, 5, 8)

        # test 6
        test_digit(246810, 6, 2)

        # test 7
        test_digit(456, 4, 0)

if __name__ == "__main__":
    main()
