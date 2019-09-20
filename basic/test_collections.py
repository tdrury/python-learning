import unittest


class CollectionsTestCase(unittest.TestCase):
    def test_dictionary(self):
        dict = {'key1': 'Value1'}
        self.assertEqual(dict['key1'], 'Value1')


if __name__ == '__main__':
    unittest.main()
