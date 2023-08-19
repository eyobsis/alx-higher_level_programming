#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_dic = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    dimr = 0
    prevalue = 0

    for letter in reversed(roman_string):

        waga = roman_dic.get(letter, 0)

        if waga >= prevalue:
            dimr += waga
        else:
            dimr -= waga

        prevalue = waga

    return dimr
