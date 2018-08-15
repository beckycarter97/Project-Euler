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


def sum_sieve_erasthones(limit):
    """Uses Sieve of Erasthones to generate all primes from 2 to n, and return
    their sum"""
    sieve_bound = math.ceil((limit - 1)/2)
    sieve = []
    for i in range(sieve_bound):
        sieve.append(False)

    cross_limit = math.ceil((math.ceil(limit) - 1) / 2)
    for i in range(1, cross_limit):
        if not sieve[i]:
            # 2i + 1 is prime, so mark all multiples
            for j in range(2*i*(i+1), sieve_bound, 2*i+1):
                sieve[j] = True

    sum = 2  # 2 is prime
    for i in range(1, sieve_bound):
        if not sieve[i]:
            sum += 2*i + 1

    return sum
