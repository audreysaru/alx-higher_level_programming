#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Get sorted keys
    sorted_keys = sorted(a_dictionary.keys())

    # Print dictionary by ordered keys
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
