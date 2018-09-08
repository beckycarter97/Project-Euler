# Problem 21 - Amicable Numbers

"""Let d(n) be defined as the sum of proper divisors of n(numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110 therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142 so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

from useful_functions import get_factors


def find_sum_divisors(n):
    sum_divisors = 0
    for divisor in get_factors(n):
        if divisor != n:
            sum_divisors += divisor

    return sum_divisors


def main():
    limit = 10000
    sum_amicable = 0
    factor_sums = [0]
    n = 1

    while n < limit:
        factor_sum = find_sum_divisors(n)
        factor_sums.append(factor_sum)
        if factor_sum < n:
            if factor_sums[factor_sum] == n:
                sum_amicable += n
                sum_amicable += factor_sum

        n += 1

    print(sum_amicable)


if __name__ == '__main__':
    main()
