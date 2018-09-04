# Problem 13
""" Work out the first ten digits of the sum of the following one-hundred
50-digit numbers - see sep file"""
# This version just actually adds them, which is boring


def main():
    numbers = []
    # read in the file, get the numbers out as strings, store in an array
    with open('Problem13_input.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            numbers.append(int(line))

    sum = 0

    for number in numbers:
        sum += number

    sum = str(sum)
    print("First ten digits of the sum are: ")
    for i in range(10):
        print(sum[i], end='')

    return


if __name__ == '__main__':
    main()
