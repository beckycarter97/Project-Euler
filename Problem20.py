# Problem 20
"""n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

from useful_functions import factorial

def main():
    result = str(factorial(100))
    digit_sum = 0

    for digit in result:
        digit_sum += int(digit)

    print(digit_sum)

if __name__ == '__main__':
    main()