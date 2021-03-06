import unittest

def bubble_sort(lst):
    '''Bubble sorts list.'''

    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1 - j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                continue
    return lst

class TestBubble(unittest.TestCase):
    def test_bubble_sort(self):
        '''Tests that the bubble sort function is produing the correct output.'''

        result = bubble_sort([6, 5, 3, 1, 8, 7, 2, 4])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()