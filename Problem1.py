# Problem 1
""" If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.Find the sum of all the
 multiples of 3 or 5 below 1000."""


def sum_mult(m, n):
    """ Finds the sum of all multiples of m below n"""
    sum = 0

    for i in range(int(n/m)):
        if ((i+1)*m < n):
            sum += (i+1)*m

    return sum


def main():
    n = 1000

    sum_mult_three = sum_mult(3, n)
    sum_mult_five = sum_mult(5, n)
    sum_mult_15 = sum_mult(15, n)

    total = sum_mult_three + sum_mult_five - sum_mult_15

    print(total)
    return total


if __name__ == "__main__":
    main()
