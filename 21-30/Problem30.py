# Problem 30

""" Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

# The fifth powers are 0^5 = 0, 1^5 = 1, 2^5 = 32, 3^5 = 243, 4^5 = 1024,
# 5^5 = 3125, 6^5 = 7776, 7^5 = 16,807, 8^5 = 32,768, 9^5 = 59,049
# How do you know when to stop looking?
# Can't be two digits bc can only use 0, 1, 2 and none of those work
# For three digits can only use up to 3, would need to use 3 because 2^6 = 64
# Four digits potentially up to 6
# Five digits + can use all of them
# Can't be brute forced at all, because there's no obvious end point?


# For any given n, if n * 9^5 has fewer than n digits, then no n digit number
# can satisfy the condition. If such an n exists, it will also be true for all
# m > n, so need to find the minimal n where this is true

def is_sum_nth_powers(num, n):
    digit_power_sum = 0

    for digit in str(num):
        digit_power_sum += int(digit)**n
        if digit_power_sum > num:
            return False

    if digit_power_sum == num:
        return True
    else:
        return False


def n_digits(m, n):
    power_sums = []

    for num in range(10**(m-1), 10**m):
        if is_sum_nth_powers(num, n):
            power_sums.append(num)

    return power_sums


def has_more_than_m_digits(n, m):
    return (10**(m-1) <= n)


def find_max_digits(p):
    digits = 1

    while (has_more_than_m_digits(digits * 9**p, digits)):
        digits = digits+1

    return digits


def sum_of_power_sums(power, printValues=False):
    maxDigits = find_max_digits(power)
    power_sums = []

    for digits in range(1, maxDigits):
        power_sums += n_digits(digits, power)

    power_sums.remove(1)

    if printValues:
        print(power_sums)

    return sum(power_sums)


def main():

    timeit.timeit(sum_of_power_sums(5))


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("sum_of_power_sums(5)",
                        setup="from __main__ import sum_of_power_sums",
                        number=1))
