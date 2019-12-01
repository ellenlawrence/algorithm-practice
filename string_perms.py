import unittest

def find_string_perms(s, b):
    '''Finds all the permutations of smaller string s inside bigger string b.'''

    for i in range(len(b) - len(s) - 1):
        


class TestStringPerms(unittest.TestCase):
    def test_find_string_perms(self):
        '''Test that the string permutation function is returning the correct
        number of permutations.'''

        result = find_string_perms('abbc', 'cbabadcbbabbcbabaabccbabc')
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()