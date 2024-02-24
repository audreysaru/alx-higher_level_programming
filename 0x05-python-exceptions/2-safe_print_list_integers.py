#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for value in my_list[:x]:
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1
        print()  # New line after printing integers
    except (ValueError, TypeError, IndexError) as e:
        traceback.print_exc() # pass # Handle the exception or perform additional actions
        raise e # Re-raise the caught exception to display the traceback

    return count
