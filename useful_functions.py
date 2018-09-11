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

    for x in range(5, int(math.sqrt(n) + 1), 6):
        # x is always of the form 6k-1, so check divisibility by x and x + 2,
        # and then increment x by 6
        if n % x == 0:
            return False
        if n % (x + 2) == 0:
            return False
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


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result


def get_proper_factors(n):
    """Finds all proper factors of a number and returns as
    array"""
    factors = [1]

    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            factors.append(x)
            if x**2 != n:
                factors.append(n // x)

    return factors
