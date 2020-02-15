# Problem 11
""" Find the greatest product of four adjacent numbers (up, down, left, right,
or diagonally) in 20x20 grid """


def largest_horiz_prod(grid, current_greatest_prod, n):
    current_row = 0
    current_col = 0

    while current_row < len(grid):
        while current_col < len(grid[0]) - n + 1:
            # print("col: {} row: {}\n".format(current_col, current_row))
            current_prod = 1
            for i in range(n):
                current_prod *= grid[current_row][current_col + i]

            if current_prod > current_greatest_prod:
                current_greatest_prod = current_prod

            current_col += 1

        current_col = 0
        current_row += 1

    return current_greatest_prod


def largest_vert_prod(grid, current_greatest_prod, n):
    current_row = 0
    current_col = 0

    while current_col < len(grid[0]):
        while current_row < len(grid) - n + 1:
            # print("col: {} row: {}\n".format(current_col, current_row))
            current_prod = 1
            for i in range(n):
                current_prod *= grid[current_row + i][current_col]

            if current_prod > current_greatest_prod:
                current_greatest_prod = current_prod

            current_row += 1

        current_row = 0
        current_col += 1

    return current_greatest_prod


def largest_right_diag_prod(grid, current_greatest_prod, n):
    current_row = 0
    current_col = 0

    while current_col < len(grid[0]) - n + 1:
        while current_row < len(grid) - n + 1:
            # print("col: {} row: {}\n".format(current_col, current_row))
            current_prod = 1
            for i in range(n):
                current_prod *= grid[current_row + i][current_col + i]

            if current_prod > current_greatest_prod:
                current_greatest_prod = current_prod

            current_row += 1

        current_row = 0
        current_col += 1

    return current_greatest_prod


def largest_left_diag_prod(grid, current_greatest_prod, n):
    current_row = 0
    current_col = len(grid[0])-1

    while current_col >= n-1:
        while current_row < len(grid) - n + 1:
            # print("col: {} row: {}\n".format(current_col, current_row))
            current_prod = 1
            for i in range(n):
                current_prod *= grid[current_row + i][current_col - i]

            if current_prod > current_greatest_prod:
                current_greatest_prod = current_prod

            current_row += 1

        current_row = 0
        current_col -= 1

    return current_greatest_prod


def main():
    grid = []
    with open('prob11grid.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            grid.append(list(map(int, line.split())))

    n = 4
    greatest_prod = 1

    greatest_prod = largest_left_diag_prod(grid, greatest_prod, n)
    print(greatest_prod)
    greatest_prod = largest_horiz_prod(grid, greatest_prod, n)
    print(greatest_prod)
    greatest_prod = largest_right_diag_prod(grid, greatest_prod, n)
    print(greatest_prod)
    greatest_prod = largest_vert_prod(grid, greatest_prod, n)
    print(greatest_prod)

    return
# Gives the wrong answer, but not sure what's wrong :/


if __name__ == '__main__':
    main()
