#!/usr/bin/python3

"""Verbose list Module"""


class VerboseList(list):
    """a list that extends the list"""

    def append(self, item):
        """Appends an item"""
        super().append(item)
        print(f"Appended list item with {item} items.")

    def extend(self, iterable):
        """extends the list"""
        super().extend(iterable)
        print(f"Extended list item with {len(iterable)} items.")

    def remove(self, item):
        """Removes the item from the list"""
        super().remove(item)
        print(f"Removed {item} from the list")

    def pop(self, item):
        """Pops an item from the list"""
        super().pop(item)
        print(f"Popped {item} from the list")
