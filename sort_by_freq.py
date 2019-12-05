import unittest

def sort_by_freq(lst):
    '''Sorts list of items by their frequency in the list and returns a list
    with the items listed by highest frequency to lowest.'''

    
    freqs = dict()
    
    for item in lst:
        freqs[item] = freqs.get(item, 0) + 1

    sorted_tuples = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

    list_by_freq = []

    for tupl in sorted_tuples:
        list_by_freq.append(tupl[0])

    return list_by_freq

class TestSortByFreq(unittest.TestCase):
    def test_sort_by_freq(self):
        '''Tests that the sort by frequency function is producing the correct
        output.'''

        result = sort_by_freq(['a', 'a', 'c', 'b', 'a', 'c'])
        self.assertEqual(result, ['a', 'c', 'b'])


if __name__ == '__main__':
    unittest.main()