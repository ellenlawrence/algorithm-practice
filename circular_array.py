"""Implement a Circular Array

A circular array is defined by having a start and indexes (be
sure to think about optimizing runtime for indexing)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.print_array()
    harry
    hermione
    ginny
    ron
    >>> circ.get_by_index(2)
    'ginny'
    >>> print(circ.get_by_index(15))
    None

However, the last item circles back around to the first item, 
so you can also rotate the list and shift the indexes. Positive
numbers rotate the list start to the right (or higher indexes)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(1)
    >>> circ.print_array()
    hermione
    ginny
    ron
    harry
    >>> circ.get_by_index(2)
    'ron'

And negative numbers rotate the list start to the left (or lower
indexes)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-1)
    >>> circ.print_array()
    ron
    harry
    hermione
    ginny
    >>> circ.get_by_index(2)
    'hermione'

And you can also rotate more than once around the ring::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-17)
    >>> circ.get_by_index(1)
    'harry'

If you add a new item after rotating, it should go at the end of
the list in its current rotation::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-2)
    >>> circ.add_item('dobby')
    >>> circ.print_array()
    ginny
    ron
    harry
    hermione
    dobby

"""


class CircularArray(object):
    """An array that may be rotated, and items retrieved by index"""

    def __init__(self):
        """Instantiate CircularArray."""

        self.circ_arr = list()
        self.head = None

    def add_item(self, item):
        """Add item to array, at the end of the current rotation."""

        if not self.head:
            self.head = 0

        self.circ_arr.insert(self.head, item)
        self.head += 1

    def get_by_index(self, index):
        """Return the data at a particular index."""

        if not self.head:
            return None

        if index >= len(self.circ_arr):
            return None
        
        if (self.head + index) < len(self.circ_arr):
            return self.circ_arr[self.head + index]

        adjusted_index = self.head + index - len(self.circ_arr) 
        return self.circ_arr[adjusted_index]

    def rotate(self, increment):
        """Rotate array, positive for right, negative for left.

        If increment is greater than list length, keep going around.  [0, 1, 2, 3, 4, 5]
        """

        if not self.head:
            return

        adjusted_index = (self.head + increment) % len(self.circ_arr)

        self.head = adjusted_index



    def print_array(self):
        """Print the circular array items in order, one per line"""

        for i in range(len(self.circ_arr)):
            print(self.get_by_index(i))

        return

if __name__ == "__main__":
    print()
    import doctest

    if doctest.testmod().failed == 0:
        print("*** ALL TESTS PASSED; YOU MUST BE DIZZY WITH JOY! ***")
    print()

