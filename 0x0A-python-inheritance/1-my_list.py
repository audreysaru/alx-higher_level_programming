#!/usr/bin/python3

"""
1-my_list.py: Module defining a class MyList that inherits from list.
"""

class MyList(list):
    """
    MyList: A class that inherits from list.

    Public Methods:
    - print_sorted(): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Returns:
            None
        """
        print(sorted(self))
