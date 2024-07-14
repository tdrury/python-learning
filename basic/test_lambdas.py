import unittest


class LambdasTestCase(unittest.TestCase):

    def test_lambda(self):
        l = lambda a, b: a * b
        self.assertEqual(l(2,5), 10)


if __name__ == '__main__':
    unittest.main()