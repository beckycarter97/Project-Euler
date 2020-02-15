# Problem 26 - Reciprocal Cycles

"""A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""

# Things found out to note:
# for any prime number p > 5 the length of the repetend of 1/p is a factor of
# p-1
# the length of the repetend of any fraction is less than or equal to one less
# than the denominator

import time


def check_next(n, longest):
    if longest > n - 1:
        return longest, False

    repetend = []
    carry = 1
    carries = {1}
    while True:
        repetend.append(int(carry*10 / n))
        carry = carry*10 % n
        if carry in carries:
            break
        elif carry == 0:
            break
        carries.add(carry)

    if len(repetend) > longest:
        return len(repetend), True
    else:
        return longest, False


def main():
    starttime = time.time()
    longest = 0
    d = 0

    for n in range(1000, 0, -1):
        longest, changed = check_next(n, longest)
        if changed:
            d = n

    print("The longest repetend occurs in 1/%d and has length %d" % (d,
                                                                     longest))
    runtime = time.time() - starttime
    print(runtime)


if __name__ == '__main__':
    main()
