# Problem 9
""" There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc"""
import math


def is_int(x):
    if math.floor(x) - x == 0:
        return True
    else:
        return False


def pythag_triple(n):
    """Finds a Pythagorean triple a,b,c such that a + b + c = 1000, and returns
    the product abc """

    # Since a and b are interchangable, and all three are at least 1, and c is
    # strictly greater than a and b, only need to check a < n/2 and b < n - 2a
    for a in range(1, math.ceil(n/2)):
        for b in range(1, n - 2*a):
            c = math.sqrt(a**2 + b**2)
            if is_int(c):
                if a + b + c == n:
                    return a*b*c

    return 0


def main():
    print(pythag_triple(1000))


if __name__ == '__main__':
    main()
