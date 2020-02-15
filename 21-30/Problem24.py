# Problem 24

"""A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?"""


from useful_functions import factorial

SOUGHT_PERMUTATION = 1000000
LIMIT = 9


def main():
    if SOUGHT_PERMUTATION > factorial(LIMIT + 1):
        raise ValueError("There are not that many permutations")
    sought_perm = []
    pos_digits = set(range(LIMIT + 1))
    skipped_opts = 0
    for num_digits in range(1, LIMIT + 2):
        num_options = factorial(LIMIT + 1 - num_digits)
        option_no = 1
        for x in pos_digits.difference(set(sought_perm)):
            if skipped_opts + (option_no * num_options) >= SOUGHT_PERMUTATION:
                sought_perm.append(x)
                skipped_opts += (option_no - 1) * num_options
                break
            option_no += 1

    for digit in sought_perm:
        print(digit, end='')


if __name__ == '__main__':
    main()
