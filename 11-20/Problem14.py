# Problem 14
"""The following iterative sequence is defined for the set of positive integers
        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is
thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""


def main():
    limit = 1000000
    collatz_lengths = [0]

    longest = 0
    start_for_longest = 0
    for i in range(1, limit):
        n = i
        length = 1

        while n > 1:
            if n < len(collatz_lengths):
                length += collatz_lengths[n] - 1
                break

            length += 1
            if n % 2 == 0:
                n = int(n/2)
            else:
                n = 3*n + 1

        collatz_lengths.append(length)

        if length > longest:
            longest = length
            start_for_longest = i

    print(start_for_longest)
    return


if __name__ == '__main__':
    main()
