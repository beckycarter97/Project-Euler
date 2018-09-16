# Problem 27
"""Euler discovered the remarkable quadratic formula:

n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive
integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by
41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces 80
primes for the consecutive values 0≤n≤79. The product of the coefficients,
−79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + a*n + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
"""

# since the primes have to start with n=0, certainly |b| must be prime
# so first thing to do is generate all the primes up to 1000?
# Also need 1 + a + b to be prime, so a must be odd, unless b is 2
# Also need 4 + 2n + b to be prime, so b can't be 2
# Basically you certainly have that when n = b, it's not prime anymore
# But basically can start by assuming |b| is a prime >= 3 and a is odd

from useful_functions import is_prime
import time

LIMIT = 1000


def get_primes(n):
    primes = [i for i in range(3, n+1) if is_prime(i)]
    return primes


def check_length(a, b):
    # Find the number of primes produced for consecutive n starting at n = 0

    for n in range(0, abs(b)):
        if not is_prime(abs(n**2 + a*n + b)):
            break

    return n


def compare_length(a, b, max_length, coeff_prod):
    length = check_length(a, b)
    if length > max_length:
                max_length = length
                coeff_prod = a*b

    return max_length, coeff_prod


def main():
    starttime = time.time()
    primes = get_primes(LIMIT)
    max_length = 0
    coeff_prod = 0

    for b in primes:
        for a in range(3, LIMIT, 2):
            max_length, coeff_prod = compare_length(a, b, max_length,
                                                    coeff_prod)
            max_length, coeff_prod = compare_length(-1 * a, b, max_length,
                                                    coeff_prod)
            max_length, coeff_prod = compare_length(a, -1 * b, max_length,
                                                    coeff_prod)
            max_length, coeff_prod = compare_length(-1 * a, -1 * b, max_length,
                                                    coeff_prod)

    print(max_length, coeff_prod)
    print(time.time() - starttime)


if __name__ == '__main__':
    main()
