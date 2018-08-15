# Problem 10 - Summation of primes

""" Find the sum of all primes below two million """
import math
from useful_functions import is_prime


def gen_primes(n):
    for i in range(n):
        if is_prime(i):
            yield i


def sum_sieve_erasthones(n):
    """Uses Sieve of Erasthones to generate all primes from 2 to n, and return
    their sum"""
    cross_limit = math.ceil(math.sqrt(n))
    sieve = []
    for i in range(n):
        sieve.append(False)

    for k in range(4, n, 2):
        # All even numbers are not prime
        sieve[k] = True

    for k in range(3, cross_limit, 2):
        if not sieve[k]:
            # n is not marked, so is prime
            for m in range(k*k, n, 2*k):
                # Mark all odd multiples of k as not prime, start at k*k
                # because for any r < k, r has a prime factor s < k, and so r*k
                # is a multiple of s, so will already be marked as not prime.
                # Similarly all even multiples are already marked as not prime.
                sieve[m] = True
    sum = 0
    for k in range(2, n):
        if not sieve[k]:
            # k is prime
            sum += k

    return sum


def main():
    print(sum_sieve_erasthones(2000000))

    return


if __name__ == '__main__':
    main()
