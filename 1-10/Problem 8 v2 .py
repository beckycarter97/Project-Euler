# Problem 8 - largest product in a series

""" The four adjacent digits in the 1000 digit number given which have the
greatest product are 9*9*8*9 = 5832. Find the thirteen adjacent digits in it
which have the greatest product. What is the value of this product? """

long_num = ("73167176531330624919225119674426574742355349194934969835203127745"
            "06326239578318016984801869478851843858615607891129494954595017379"
            "58331952853208805511125406987471585238630507156932909632952274430"
            "43557668966489504452445231617318564030987111217223831136222989342"
            "33803081353362766142828064444866452387493035890729629049156044077"
            "23907138105158593079608667017242712188399879790879227492190169972"
            "08880937766572733300105336788122023542180975125454059475224352584"
            "90771167055601360483958644670632441572215539753697817977846174064"
            "95514929086256932197846862248283972241375657056057490261407972968"
            "65241453510047482166370484403199890008895243450658541227588666881"
            "16427171479924442928230863465674813919123162824586178664583591245"
            "66529476545682848912883142607690042242190226710556263211111093705"
            "44217506941658960408071984038509624554443629812309878799272442849"
            "09188845801561660979191338754992005240636899125607176060588611646"
            "71094050775410022569831552000559357297257163626956188267042825248"
            "3600823257530420752963450")


def reset_current_prod(pos, n):
    product = 1
    done = False

    while not done:
        if pos >= len(long_num) - n + 1:
            break

        for i in range(n):
            product *= int(long_num[pos+i])

        if product == 0:
            product = 1
        else:
            done = True
        pos += 1

    return pos, product


def largest_product(n):
    current_greatest_product = 1
    current_pos, current_prod = reset_current_prod(0, n)

    while current_pos < len(long_num) + 1 - n:
        # As soon as encounter a 0, can skip over any products which contain it
        # Then need to reset the current product value
        if long_num[current_pos+n-1] == '0':
            current_pos += n
            current_pos, current_prod = reset_current_prod(current_pos, n)
        elif long_num[current_pos-1] == '0':
            current_pos, current_prod = reset_current_prod(current_pos, n)
            current_pos
        else:
            current_prod /= int(long_num[current_pos - 1])
            current_prod *= int(long_num[current_pos + n - 1])
            current_pos += 1

        if current_prod > current_greatest_product:
            current_greatest_product = current_prod

    return current_greatest_product


def main():
    n = 13
    print("Largest product of {} numbers is {}".format(n, largest_product(n)))


if __name__ == '__main__':
    main()
