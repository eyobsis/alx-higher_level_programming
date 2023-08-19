#!/usr/bin/python3


def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common_elements = set()

    # Iterate over each element in set_1
    for elm in set_1:
        # Check if the element is present in set_2
        if elm in set_2:
            # Add the common element to the common set
            common_elements.add(elm)

    return common_elements
