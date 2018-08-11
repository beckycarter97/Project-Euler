# Problem 4 - Largest palindromic product

""" A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
"""


def ispalindrome(s):
    """ Tests if a string s is a palindrome"""
    palindrome = True

    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            palindrome = False
            break

    return palindrome


def change_nums(num1, num2):
    num2 -= 1
    num1 = num2
    return num1, num2


def main():
    num1 = 999
    num2 = 999

    palindrome = 0
    done = False

    while not done:
        product = num1 * num2

        if product < palindrome:
            num1, num2 = change_nums(num1, num2)

        elif ispalindrome(str(product)):
            palindrome = product
            num1, num2 = change_nums(num1, num2)

        else:
            num1 -= 1

        if num1 < 100:
            num1, num2 = change_nums(num1, num2)

        if num2 < 100:
            done = True

    print(palindrome)

    return


if __name__ == '__main__':
    main()
