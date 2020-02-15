# Problem 17
"""If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage."""


# 1 to 9 will be used several times, so useful to have this figure saved
# The teens are weird, so need to be done a bit separately
# For each set of blah-ty something, you get the length of blahty, then
# 'blahty and' 9 times, and then the words for 1 to 9
# For each x hundred, get'x hundred' once and get 'x hundred and' 99 times,
# plus the words for all the numbers 1 - 99


def main():
    # First calculate the lengths of the key words used in numbers
    units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine']
    len_units = []
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    len_teens = []
    mults_ten = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
                 'eighty', 'ninety']
    len_mults_ten = []

    for unit in units:
        len_units.append(len(unit))
    for teen in teens:
        len_teens.append(len(teen))
    for mult_ten in mults_ten:
        len_mults_ten.append(len(mult_ten))

    # Letters used for numbers 1-9 and 10-19 summed directly
    one_to_nine = 0
    for num_len in len_units:
        one_to_nine += num_len

    ten_to_nineteen = 0
    for num_len in len_teens:
        ten_to_nineteen += num_len

    # For each set of 10 numbers 20-29, 30-29, ..., 90-99 the same pattern:
    # The word 'twenty' appears 10 times, as do all of the words in 1-9
    # so 20-99 contains the words of 1-9 eight times, and each word 'twenty',
    # 'thirty' etc ten times
    one_to_99 = 0
    one_to_99 += one_to_nine
    one_to_99 += ten_to_nineteen
    one_to_99 += 8*(one_to_nine)
    for num_len in len_mults_ten:
        one_to_99 += num_len*10

    # For each set of 100 numbers 100-199, 200-299 etc there is a pattern:
    # The word 'one' or 'two' etc appears 100 times, as does the word 'hundred'
    # The word 'and' appears 99 times, and all the words for 1-99 appear
    one_to_999 = 0
    one_to_999 += one_to_99
    one_to_999 += 9*(len('hundred') * 100 + len('and') * 99 + one_to_99)
    one_to_999 += 100*one_to_nine

    # It then simply remains to add the letters in 'One thousand'
    total = one_to_999 + len('One') + len('thousand')

    print(total)

    return


if __name__ == '__main__':
    main()
