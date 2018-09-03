# Problem 12
"""What is the value of the first triangle number to have over five hundred
divisors"""

import math


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


def get_num_factors(number):
    """Finds the number of factors of any number - note includes
    non prime factors"""
    return len(get_factors(number))


def get_triangle_num(n):
    return int(n*(n+1)/2)


def main():
    n = 1

    while True:
        triangle_num = get_triangle_num(n)
        num_factors = get_num_factors(triangle_num)
        if num_factors > 500:
            break

        n += 1

    print("Answer: {}".format(triangle_num))

    return


if __name__ == '__main__':
    main()
