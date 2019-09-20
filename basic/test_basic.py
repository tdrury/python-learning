import unittest

class BasicLanguageTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_types(self):
        arg1 = "1"
        arg2 = 1
        self.assertNotEqual(arg1, arg2)
        self.assertEqual(arg1, str(arg2))
        self.assertEqual(int(arg1), arg2)


if __name__ == '__main__':
    unittest.main()
