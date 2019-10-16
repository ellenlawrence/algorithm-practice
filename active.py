"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""


    # MY ORIGINAL SOLUTION (DOESN'T PASS SECOND TEST)
    # dct = dict()

    # for author in bio_data:
    #     for year in range(author[1], (author[2] + 1)):
    #         dct[year] = dct.get(year, 0) + 1
    
    # year_range = []
    # for y, n in dct.items():
    #     if n == max(dct.values()):
    #         year_range.append(y)
    # year_range.sort()
    # return (year_range[0], year_range[-1])


    # BEST SOLUTION:

    century = [0] * 100

    for person, start, end in bio_data:
        for year in range(start, (end + 1)):
            century[year - 1900] += 1










if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")