#!/usr/bin/python3
"""a class MyList that inherits from list
"""


class MyList(list):
    """A class that inherits from list
    """

    def print_sorted(self):
        """
	Prints self in sorted format
        """
        print(sorted(self))
