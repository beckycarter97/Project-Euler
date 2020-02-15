# Problem 25

"""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?"""

SOUGHT_LENGTH = 1000


def get_fib_no(index, fib_nos=[0, 1, 1]):
    try:
        prev_fib = fib_nos[index - 1]
    except:
        prev_fib = get_fib_no(index - 1, fib_nos)

    try:
        prev_two_fib = fib_nos[index - 2]
    except:
        prev_two_fib = get_fib_no(index - 2, fib_nos)

    return prev_fib + prev_two_fib


def main():
    fib_nos = [0, 1, 1]

    for x in range(3, 10**SOUGHT_LENGTH):
        x_fib = get_fib_no(x, fib_nos)
        fib_nos.append(x_fib)

        if len(str(x_fib)) == SOUGHT_LENGTH:
            print(x)
            break


if __name__ == '__main__':
    main()
