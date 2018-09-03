# This solution is from the overview document, I didn't come up with the
# algorithm

import math


def sieve_erasthones(n):
    """Returns array of all primes less than n"""
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
    primes = []
    for k in range(2, n):
        if not sieve[k]:
            # k is prime

            primes.append(k)

    return primes


def main():
    n = 3  # any prime
    Dn = 2  # number of divisors of n
    cnt = 0

    P = 1000
    prime_array = sieve_erasthones(P)
    no_primes = len(prime_array)

    while cnt <= 500:
        n += 1
        n_1 = n
        if (n % 2 == 0):
            n_1 = n_1 / 2
        Dn_1 = 1
        for i in range(no_primes):
            if prime_array[i]*prime_array[i] > n_1:
                Dn_1 *= 2
                break
            # When the prime divisor would be greater than the residual n_1
            # that residual n_1 is the last prime factor with an exponent =1
            # there is no need to identify it
            exponent = 1
            while (n_1 % prime_array[i]) == 0:
                exponent += 1
                n_1 /= prime_array[i]
            if exponent > 1:
                Dn_1 *= exponent
            if n_1 == 1:
                break
        cnt = Dn*Dn_1
        Dn = Dn_1
    print(n*(n-1)/2)


if __name__ == '__main__':
    main()
