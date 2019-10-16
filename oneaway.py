"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    if w1 == w2:
        return True

    if abs(len(w1) - len(w2)) > 1:
        return False

    if len(w2) > len(w1):
        w1, w2 = w2, w1

    edits = 0
    i = j = 0

    while j < len(w2):

        if w1[i] != w2[j]:
            
            edits += 1
            if edits > 1:
                return False
            i += 1

            if len(w1) == len(w2):
                j += 1
        else:
            i += 1
            j += 1

    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
