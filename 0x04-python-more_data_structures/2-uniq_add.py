#!/usr/bin/python3


def uniq_add(my_list=[]):
    # Create an empty set
    theunik_set = set()

    # Iterate over each element in the input list
    for number in my_list:
        # if the int is not already in the set
        if number not in theunik_set:
            theunik_set.add(number)

    # sum of the unique ints
    the_sum = sum(theunik_set)

    return the_sum
