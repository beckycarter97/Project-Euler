# Problem 16
"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""


def main():
    result = 0

    for digit in str(2**1000):
        result += int(digit)

    print(result)
    return


if __name__ == '__main__':
    main()
