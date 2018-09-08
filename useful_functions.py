# A file in which to keep any useful functions for reuse in other problems

import math


def is_prime(n):
    """ Using facts 1- 1 is not prime
                    2- 2 is the only even prime
                    3- All primes > 3 can be written in form 6k +- 1
                    4- Any number n can have only one primefactor > sqrt(n) """

    if n == 1:
        return False
    elif n < 4:
        return True

    elif n % 2 == 0:
        return False

    if (n+1) % 6 != 0:
        # n not of the form 6k -1
        if (n-1) % 6 != 0:
            # n also not of the form 6k+1
            return False

    limit = math.floor(math.sqrt(n))
    test = 5  # above ensures n is of form 6k+-1 so is not divisible by 2 or 3

    while test <= limit:
        # test is always of the form 6k-1, so check divisibility by test and
        # test + 2, and then increment t by 6
        if n % test == 0:
            return False
        if n % (test + 2) == 0:
            return False
        test += 6

    return True


def bubble_sort(list):
    for limit in range(len(list) - 1, 0, -1):
        for i in range(0, limit):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

    return list


def yield_primes(number):
    """Yields primes bigger than or equal to number"""
    while True:
        if is_prime(number):
            yield number


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


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result


def get_factors(number):
    """Finds all factors of a number (not just prime ones) and returns as
    array"""
    factors = []
    limit = math.floor(math.sqrt(number))
    factor = 1

    while factor < limit:
        if number % factor == 0:
            second_factor = int(number/factor)
            if not(factor in factors):
                factors.append(factor)
            if not (second_factor in factors):
                factors.append(second_factor)

        factor += 1
    return factors
