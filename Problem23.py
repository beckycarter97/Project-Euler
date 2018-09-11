# Problem 23 - Non Abundant Sums

"""A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers."""

import math
import time

UPPER_LIM = 28123
LOWER_LIM = 12


def get_proper_factors(number):
    """Finds all proper factors of a number and returns as
    array"""
    factors = [1]
    limit = math.ceil(math.sqrt(number))
    factor = 2

    while factor < limit:
        if number % factor == 0:
            second_factor = int(number/factor)
            if not(factor in factors):
                factors.append(factor)
            if not (second_factor in factors):
                factors.append(second_factor)

        factor += 1
    return factors


def is_abundant(n):
    factor_sum = sum(get_proper_factors(n))

    if factor_sum > n:
        return True
    else:
        return False


def get_abundant_nums():
    upper_lim = UPPER_LIM - LOWER_LIM + 1
    abundant_nums = []

    for cur_num in range(LOWER_LIM, upper_lim):
        if is_abundant(cur_num):
            abundant_nums.append(cur_num)

    return abundant_nums


def main():
    non_abundant_sum = 0
    abundant_nums = get_abundant_nums()

    nums = [False for i in range(UPPER_LIM + 1)]

    for index in range(len(abundant_nums)):
        first_num = abundant_nums[index]
        for second_num in abundant_nums[index:-1]:
            abundant_sum = first_num + second_num
            if abundant_sum > UPPER_LIM:
                break
            nums[abundant_sum] = True

    for i in range(len(nums)):
        if not nums[i]:
            non_abundant_sum += i

    print(non_abundant_sum)

    return


if __name__ == '__main__':
    main()
