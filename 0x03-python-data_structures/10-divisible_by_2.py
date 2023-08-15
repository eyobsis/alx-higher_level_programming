#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    ms = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            ms.append(True)
        else:
            ms.append(False)

    return (ms)
