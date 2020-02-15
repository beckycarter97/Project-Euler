# Problem 22
"""Using names.txt(right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def bubble_sort(list):
    for limit in range(len(list) - 1, 0, -1):
        for i in range(0, limit):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

    return list


def read_names():
    names = []
    with open("Problem_22names.txt") as f:
        line = f.readline()
        for name in line.split(","):
            name = name.strip('" ')
            names.append(name)

    return names


def get_letter_val(letter):
    values = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
              "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
              "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
              "W": 23, "X": 24, "Y": 25, "Z": 26}

    return values[letter]


def get_alpha_val(name):
    alpha_val = 0

    for letter in name:
        alpha_val += get_letter_val(letter)

    return alpha_val


def main():
    names = read_names()
    names = bubble_sort(names)

    total_name_scores = 0

    for i in range(len(names)):
        total_name_scores += (i+1) * get_alpha_val(names[i])

    print(total_name_scores)


if __name__ == '__main__':
    main()
