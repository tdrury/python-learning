import unittest


class TypeConversionTestCase(unittest.TestCase):

    def test_string_to_int(self):
        s = "3"
        self.assertEqual(int(s)+1, 4)

    def test_string_to_int_bad(self):
        s = "a3"
        with self.assertRaises(Exception):
            int(s)+1

    def test_string_to_float(self):
        s = "3.14"
        self.assertEqual(float(s)*2, 6.28)

    def test_int_to_string(self):
        i = 3
        self.assertEqual(str(i)+"foo", "3foo")


if __name__ == '__main__':
    unittest.main()
