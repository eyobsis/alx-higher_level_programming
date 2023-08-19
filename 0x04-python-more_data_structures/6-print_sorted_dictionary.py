#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    z_kulf = sorted(a_dictionary.keys())

    for key in z_kulf:
        waga = a_dictionary[key]
        print("{}: {}".format(key, waga))
