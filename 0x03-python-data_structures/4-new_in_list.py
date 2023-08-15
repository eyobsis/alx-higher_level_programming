#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    d_plicated = [i for i in my_list]
    d_plicated[idx] = element
    return (d_plicated)
