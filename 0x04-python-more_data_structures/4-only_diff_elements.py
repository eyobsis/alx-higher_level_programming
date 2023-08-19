#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    dif_elm = set()

    for j in set_1:
        if j not in set_2:
            dif_elm.add(j)

    for j in set_2:
        if j not in set_1:
            dif_elm.add(j)

    return dif_elm
