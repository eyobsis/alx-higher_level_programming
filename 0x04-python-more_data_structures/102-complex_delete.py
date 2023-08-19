#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    keys_todel = []

    for key, val in a_dictionary.items():
        if val == value:
            keys_todel.append(key)

    for key in keys_todel:
        del a_dictionary[key]

    return a_dictionary
