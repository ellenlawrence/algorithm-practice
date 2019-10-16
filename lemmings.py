"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    distances2 = []
    for hole in range(0, num_holes):
        distances1 = []
        for cafe in cafes:
            distance = abs(hole - cafe)
            distances1.append(distance)
        distances2.append(min(distances1))

    return max(distances2)






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
