# Problem 15 - Lattice Paths
"""Starting in the top left corner of a 2×2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?"""

# In total in an nxn grid, it is necessary to got right n times, and down n
# times. These moves can be made in any order, so this is simply a
# combinatorics question, with the number of routes through an nxn grid being
# 2n!/(n!)^2


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result


def main():
    n = 20
    numerator = factorial(2*n)
    denom = factorial(n)
    denom = denom**2
    num_routes = numerator / denom

    print(num_routes)
    return


if __name__ == '__main__':
    main()
