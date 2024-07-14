import unittest


class CollectionsTestCase(unittest.TestCase):

    def test_dictionary(self):
        dic = {'key1': 'Value1'}
        self.assertEqual(dic['key1'], 'Value1')

    def test_list(self):
        l = ["a", "b", "c", 2, 3.14]
        self.assertEqual(l[0], "a")
        self.assertEqual(l[4], 3.14)
        self.assertEqual(len(l), 5)
        self.assertTrue(isinstance(l, list))


if __name__ == '__main__':
    unittest.main()
