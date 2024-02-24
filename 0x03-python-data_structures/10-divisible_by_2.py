#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Return a new list with T or F for each element in the orig list
    return [num % 2 == 0 for num in my_list]
