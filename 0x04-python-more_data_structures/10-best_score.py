#!/usr/bin/python3


def best_score(a_dictionary):
    # Check if the dictionary is empty or None
    if not a_dictionary:
        return None

    # Get the key with the maximum value
    maxval_key = max(a_dictionary, key=a_dictionary.get)

    # Return the key with the largest integer value
    return maxval_key
