"""
>>> make_golf_roster([('Ellen', 100), ('Scott', 80), ('Kristine', 60), ('Kyle', 75), ('Peachie', 90), ('Binkie', 90)]) 
[('E', 1), ('P', 2), ('B', 2), ('S', 4), ('K', 5), ('K', 6)]

"""

def make_golf_roster(scores):
    """turns tuples with names and scores into a golf roster."""

    def key_func(item):
        return item[1]


    sorted_scores = sorted(scores, key=key_func, reverse=True)

    golf_roster = []

    for i, score in enumerate(sorted_scores):

        if not golf_roster or sorted_scores[i][1] != sorted_scores[i-1][1]:
            golf_roster.append((score[0][0], i+1))

        else:
            golf_roster.append((score[0][0], golf_roster[i-1][1]))

    return golf_roster




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n")