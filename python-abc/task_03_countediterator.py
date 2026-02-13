#!/usr/bin/python3
"""Counted iterator module question"""


class CountedIterator:
    """Counted iterator class"""
    def __init__(self, iterable):
        self._iter = iter(iterable)
        self._counter = 0

    def __iter__(self):
        """returns the iterator"""
        return self

    def __next__(self):
        """Return the next item and increment the counter"""
        try:
            item = next(self.iter)
            self._counter += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """return the counter's value"""
        return self.counter
