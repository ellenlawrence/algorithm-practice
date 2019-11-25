import unittest

def bubble_sort(lst):
    '''Bubble sorts list.'''



class TestBubble(unittest.TestCase):
    def test_bubble_sort(self):
        '''Tests that the bubble sort function is produing the correct output.'''

        result = bubble_sort([6, 5, 3, 1, 8, 7, 2, 4])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()