# A file in which to keep any useful functions for reuse in other problems

import math


def is_prime(n):
    """ Using facts 1- 1 is not prime
                    2- 2 is the only even prime
                    3- All primes > 3 can be written in form 6k +- 1
                    4- Any number n can have only one primefactor > sqrt(n) """

    if n == 1 or n < 4:
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
