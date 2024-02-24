#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list with the same elements as the input list
    new_list = [element for element in my_list]

    # Replace all occurrences of 'search' with 'replace' in the new list
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace

    return new_list
