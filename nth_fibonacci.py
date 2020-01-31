import unittest

def n_fib(n):
    '''Returns the nth number in the Fibonacci sequence.'''

    if n <= 0:
        raise ValueError('Input must be greater than 0')
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return n_fib(n-1) + n_fib(n-2)
    # time complexity is O(n)

class TestFib(unittest.TestCase):
    def test_n_fib(self):
        '''Test that the fibonacci function is producing correct output.'''

        result = n_fib(7)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()