# Problem 6 - Sum square difference

"""The sum of the squares of the first ten natural numbers is, 385. The square
of the sum of the first ten natural numbers is, 3025. Hence the difference
between the sum of the squares of the first ten natural numbers and the square
of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum."""


def sum_nums(n):
    return n*(n+1)/2


def sum_squares(n):
    return n*(n + 1)*(2*n + 1)/6


def main():
    n = 100
    sum_diff = (sum_nums(n))**2 - sum_squares(n)

    print(sum_diff)


if __name__ == '__main__':
    main()
