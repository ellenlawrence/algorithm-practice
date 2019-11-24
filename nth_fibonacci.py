import unittest

def n_fib(n):
    '''Returns the nth number in the Fibonacci sequence.'''







class TestFib(unittest.TestCase):
    def test_n_fib(self):
        '''Test that the fibonacci function is producing correct output.'''

        result = n_fib(7)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()