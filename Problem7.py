# Problem 7 - 1001st prime
""" What is the 10001st prime number? """

from useful_functions import is_prime


def nth_prime(n):
    """ Finds nth prime for any n, using that all primes greater than 3 are
        of the form 6k+-1"""
    if n == 1:
        return 2
    elif n == 2:
        return 3

    primes_found = 2
    test = 5
    largest_prime = 3

    while primes_found < n:
        if is_prime(test):
            primes_found += 1
            largest_prime = test
            if primes_found == n:
                break

        if is_prime(test + 2):
            primes_found += 1
            largest_prime = test + 2

        test += 6

    return largest_prime


def main():
    print(nth_prime(10001))

    return


if __name__ == '__main__':
    main()
