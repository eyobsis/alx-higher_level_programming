#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = sum(score * weight for score, weight in my_list)
    denom = sum(weight for _, weight in my_list)

    return num / denom
