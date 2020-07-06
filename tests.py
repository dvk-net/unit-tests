import unittest

from funcs import my_mean


class TestMyMean(unittest.TestCase):

    def test_my_mean_one_int(self):
        self.assertEqual(my_mean([1,]), 1)
    
    def test_my_mean_many_ints(self):
        self.assertEqual(my_mean([1, 2, 3]), 2)
    
    def test_my_mean_many_floats(self):
        self.assertEqual(my_mean([1.1, 2.2, 3.3]), 6.6/3)

    def test_my_mean_empty_list(self):

        with self.assertRaises(ZeroDivisionError):
            res = my_mean([])


if __name__ == '__main__':
    unittest.main()