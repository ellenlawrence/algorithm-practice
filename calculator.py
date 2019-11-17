"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""

    items = s.split()

    operator2 = int(items.pop())

    while items:
        operator1 = int(items.pop())
        operator = items.pop()

        if operator == '+':
            operator2 = operator1 + operator2
        if operator == '-':
            operator2 = operator1 - operator2
        if operator == '*':
            operator2 = operator1 * operator2
        if operator == '/':
            operator2 = int(operator1 / operator2)

    return operator2        



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
