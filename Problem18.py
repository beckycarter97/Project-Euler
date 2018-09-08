# Problem 18

"""By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires
a clever method! ;o)"""


def read_in_triangle():
    triangle = []
    with open('prob18triangle.txt') as f:
        for line in f:
            tr_line = []
            for num in line.split():
                tr_line.append(int(num))
            triangle.append(tr_line)

    return triangle


def fill_in_row(triangle_row, path_triangle_prev_row):
    next_path_row = []

    # First element in row can only be reached by the first element in row above
    next_path_row.append(triangle_row[0] + path_triangle_prev_row[0])

    cur_item = 1
    while cur_item < len(triangle_row) - 1:
        # ith element can be reached from ith or (i-1)th element of prev row (0 < i < len(row))
        left_item = path_triangle_prev_row[cur_item-1]
        right_item = path_triangle_prev_row[cur_item]

        if left_item > right_item:
            next_path_row.append(left_item + triangle_row[cur_item])
        else:
            next_path_row.append(right_item + triangle_row[cur_item])

        cur_item += 1

    # last element can only be reached from last element of previous row
    # (which has index 1 smaller)
    next_path_row.append(triangle_row[cur_item] + path_triangle_prev_row[cur_item -1])

    return next_path_row


def main():
    triangle = read_in_triangle()
    triangle_len = len(triangle)
    path_triangle = []

    path_triangle.append(triangle[0])
    cur_row =1

    while cur_row < triangle_len:
        next_path_row = fill_in_row(triangle[cur_row], path_triangle[cur_row -1])
        path_triangle.append(next_path_row)
        cur_row += 1

    longest_path = 0
    for path_length in path_triangle[triangle_len - 1]:
        if path_length > longest_path:
            longest_path = path_length

    print(longest_path)
    return

if __name__ == '__main__':
    main()
