'''tests for intro-to-python labs'''

import unittest

class TestLabMethods(unittest.TestCase):
    '''tests for lab answers'''

    def test_counting(self):
        '''tests the `counting` module'''
        import counting

        results = counting.count()

        self.assertListEqual(results, [1, 2, 3, 4, 5])

    def test_more_counting(self):
        '''tests the `more_counting` module'''
        import more_counting

        self.assertListEqual(more_counting.count(2), [1, 2])
        self.assertListEqual(more_counting.count(5), [1, 2, 3, 4, 5])

    def test_evens(self):
        '''tests the `evens` module'''
        import evens

        self.assertEqual(evens.evens([1, 2, 3, 4]), 6)
        self.assertEqual(evens.evens([1, 3, 5]), 0)
        self.assertEqual(evens.evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)

    def test_tuples(self):
        '''tests the `tuples` module'''
        import tuples

        self.assertEqual(tuples.partition(3), (None, 3))
        self.assertEqual(tuples.partition(4), (4, None))

        results_1 = tuples.partition_list([1, 4, 2, 6, 3, 8])
        self.assertEqual(results_1, ([1, 3], [4, 2, 6, 8]))

        results_2 = tuples.partition_list([1, 3, 5, 7, 9])
        self.assertEqual(results_2, ([1, 3, 5, 7, 9], []))

if __name__ == '__main__':
    unittest.main()
