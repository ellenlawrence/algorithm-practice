import unittest

def sort_by_freq(lst):
    '''Sorts list of items by their frequency in the list and returns a list
    with the items listed by highest frequency to lowest.'''




class TestSortByFreq(unittest.TestCase):
    def test_sort_by_freq(self):
        '''Tests that the sort by frequency function is producing the correct
        output.'''

        result = sort_by_freq(['a', 'a', 'c', 'b', 'a', 'c'])
        self.assertEqual(result, ['a', 'c', 'b'])


if __name__ == '__main__':
    unittest.main()