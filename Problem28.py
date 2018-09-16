# Problem 28 - Number Spiral Diagonals

""" Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""

# For any odd n can construct nxn spiral as such, and have
# The upper right diagonal consists of the odd squares
# The lower left diagonal consists of the even squares plus 1
# The upper left diagonal numbers are (the odd square - the odd no + 1)
# The lower right diagonal numbers are (the even squares - the even no - 1)

SIZE = 1001


def main():
    diag_sum = 1

    for odd_no in range(3, SIZE + 1, 2):
        diag_sum += odd_no**2                   # For upper right diagonal
        diag_sum += odd_no**2 - odd_no + 1      # For upper left diagonal
    for even_no in range(2, SIZE + 1, 2):
        diag_sum += even_no**2 + 1              # For lower left diagonal
        diag_sum += even_no**2 - even_no + 1    # For lower right diagonal

    print(diag_sum)


if __name__ == '__main__':
    main()
