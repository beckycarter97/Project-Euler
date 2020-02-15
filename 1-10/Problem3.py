# Problem 3 - Largest prime factor

""" The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
factor of 600851475143 """


def prime_factor(n):
    """ Finds the prime factors of n and returns as an array """
    factors = []
    trial = 2

    while n > 1:
        rem = n % trial

        if rem == 0:
            factors.append(trial)
            n = n / trial

        else:
            trial += 1

    return factors


def main():
    test = 600851475143

    factors = prime_factor(test)

    print("The largest prime factor of {} is {}".format(test, factors[-1]))


if __name__ == '__main__':
    main()
