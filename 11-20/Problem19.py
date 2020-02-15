# Problem 19 - Counting Sundays

"""You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.


A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400. How many Sundays fell on the first of the month
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""


def is_leap_year(year):
    if year % 4 != 0:
        leap_year = False
    else:
        if year % 100 == 0 and year % 400 != 0:
            leap_year = False
        else:
            leap_year = True

    return leap_year


def month_length(month_num, year):
    if month_num == 2:
        if is_leap_year(year):
            length = 29
        else:
            length = 28
    elif (month_num == 4) or \
         (month_num == 6) or \
         (month_num == 9) or \
         (month_num == 11):
        length = 30
    else:
        length = 31

    return length


def main():
    num_sundays = 0

    cur_year = 1901
    cur_month = 1  # numbering months 1-12 as standard
    cur_day = 2  # numbering days 0 - 6 where 0 is Sunday

    while cur_year <= 2000:
        # If current month starts on a Sunday, incremement count
        if cur_day == 0:
            num_sundays += 1

        # Then increase cur_day and cur_month values appropriately, to move to
        # next month
        cur_day += month_length(cur_month, cur_year)
        cur_day = cur_day % 7
        cur_month += 1
        # When necessary, incrememnt cur_year and resest cur_month
        if cur_month > 12:
            cur_year += 1
            cur_month = (cur_month % 12)

    print(num_sundays)

if __name__ == '__main__':
    main()
