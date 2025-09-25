#!/usr/bin/env python3
"""
This module defines the CountedIterator class, which wraps a standard iterator
and keeps track of how many items have been iterated over.
"""


class CountedIterator:
    """Custom iterator that counts how many times it has been iterated."""

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.

        Args:
            iterable: Any iterable object to wrap.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            self: So it can be used in for-loops and other iterable contexts.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Returns:
            The next item in the wrapped iterator.

        Raises:
            StopIteration: When the wrapped iterator is exhausted.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated.

        Returns:
            int: Number of successful calls to __next__().
        """
        return self.count
