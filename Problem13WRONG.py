# Problem 13
""" Work out the first ten digits of the sum of the following one-hundred
50-digit numbers - see sep file"""
# THIS VERSION DOES NOT WORK
# Have kept because I think the add_carry function is actually quite good,
# and that does work, and also just for reference
# It does work with pretty high probability though - the likelihood of the
# 13th digit sum affect the first 10 digits of the sum, is quite small
# and the probability of the nth digit (n > 11) affecting the first 10 digits
# decreases as n increases. So it will probably work, but not for certain
# The idea is probably more useful for longer numbers, where calculating the
# whole sum would be impractical.


def add_carry(sum_digits, carry, index, extended=False):
    """Given an array sum_digits of integers, adds the value carry, in the
    position index, such that each value in the array is a an integer between
    0 and 9. The boolean extended is used to track whether a new digit was
    inserted at the beginning, due to the recursive nature of the function"""
    if index < 0:
        sum_digits.insert(0, carry)
        extended = True

    else:
        old_digit = int(sum_digits[index])
        new_digit = old_digit + carry

        if new_digit >= 10:
            carry = int((new_digit - new_digit % 10) / 10)
            new_digit = new_digit % 10
            extended = add_carry(sum_digits, carry, index - 1)
        if extended:
            # A new digit was added at the beginning of number, at some point
            # in this stack of calls to add_carry, so index value must be
            # incremented to allow for this
            sum_digits[index + 1] = new_digit
        else:
            sum_digits[index] = new_digit
    return extended


def main():
    numbers = []
    sum_digits = []
    # read in the file, get the numbers out as strings, store in an array
    with open('Problem13_input.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            numbers.append(line)

    for i in range(50):
        digit_sum = 0
        for num in numbers:
            digit = int(num[i])
            digit_sum += digit

        if digit_sum >= 10:
            carry = int((digit_sum - digit_sum % 10)/10)
            digit_sum = digit_sum % 10
            if not sum_digits:
                sum_digits = [carry]
            else:
                last_index = len(sum_digits) - 1
                add_carry(sum_digits, carry, last_index)

        # if len(sum_digits) > 11 and digit_sum < 9:
            # THIS DOES NOT WORK - CAN HAVE A CARRY OF MORE THAN 1
            # break

        sum_digits.append(digit_sum)

    for i in range(10):
        print(sum_digits[i], end='')
    return


if __name__ == '__main__':
    main()
