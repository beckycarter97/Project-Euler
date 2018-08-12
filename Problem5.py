# Problem 5 - Smallest Multiple

"""2520 is the smallest number that can be divided by each of the numbers from
   1 to 10 without any remainder. What is the smallest positive number that is
   evenly divisible by all of the numbers from 1 to 20?"""


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def highest_exponent(p, n):
    """ Finds the highest exponent of prime p which is less than or equal to n
    """
    k = 1
    found = False

    while not found:
        if p**k > n:
            k -= 1
            found = True
        else:
            k += 1

    return k


def small_mult(n):
    """ Finds the smallest number which can be divided by each of the numbers
        from 1 to n without any remainder """

    factor_list = []

    for i in range(2, n+1):
        if not is_prime(i):
            continue
        k = highest_exponent(i, n)
        factor_list.append(i**k)

    smallest_mult = 1

    for factor in factor_list:
        smallest_mult *= factor

    return smallest_mult


def main():
    print(small_mult(20))


if __name__ == '__main__':
    main()
