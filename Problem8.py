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


# Once you got some set of n numbers, moving along one only increases product
# if the number you gain is bigger than the number you lose. So it's easy to
# tell if the next one along is an improvement. Also would need to keep an eye
# on the array that's best so far. To make comparison easier probably want to
# store that with digits increasing? For a new set to be better would need each
# digit in new array to be >= one in old array. Again sort in increasing order
# then can compare more easily

# So start with first four, set these as current best. At any point check if
# moving on will increase product, if so check if its better. To do so, sort it
# and then compare with current best

# So need a good sorting algorithm


def bubble_sort(list):
    for limit in range(len(list) - 1, 0, -1):
        for i in range(0, limit):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

    return list


def get_sorted_integer_array(i, n):
    integer_array = []

    for j in range(n):
        integer_array.append(int(long_num[i+j]))

    bubble_sort(integer_array)

    return integer_array


def is_greater_eq(list1, list2, list_len):
    # Compares two sorted integer lists
    for i in range(list_len):
        if list1[i] < list2[i]:
            return False
    return True


def largest_product(n):
    print("Largest Product n = {}".format(n))
    potential_greater_array = []
    current_greatest_array = get_sorted_integer_array(0, n)
    current_pos = 1

    while current_pos < len(long_num) - n + 1:
        # print(current_pos)
        if long_num[current_pos+n-1] > long_num[current_pos-1]:
            # When move along one digit in the number, the set of n digits
            # looking at only varies by one number, so only compare these two
            # to see if current move improves over previous. Only then do we
            # compare to our overall greatest array
            potential_greater_array = get_sorted_integer_array(current_pos, n)
            if is_greater_eq(potential_greater_array,
                             current_greatest_array, n):
                current_greatest_array = potential_greater_array

        current_pos += 1

    largest_product = 1

    for i in range(n):
        largest_product *= current_greatest_array[i]

    return largest_product


def main():
    print(largest_product(13))


if __name__ == '__main__':
    main()
