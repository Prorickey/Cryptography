import unittest
from utilities import chi_squared, mod_inverse, text_clean, text_block, gcd

class TestUtilities(unittest.TestCase):

    def test_gcd(self):
        # Basic test cases
        self.assertEqual(gcd(10, 5), 5)
        self.assertEqual(gcd(20, 10), 10)
        self.assertEqual(gcd(100, 25), 25)
        self.assertEqual(gcd(7, 3), 1)
        self.assertEqual(gcd(18, 12), 6)
        self.assertEqual(gcd(42, 56), 14)
        self.assertEqual(gcd(27, 9), 9)
        self.assertEqual(gcd(81, 27), 27)

        # Edge cases
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(0, 0), 0)  # Assuming gcd(0, 0) returns 0
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(123456789, 987654321), 9)
        
        # Large numbers
        self.assertEqual(gcd(1000000000, 500000000), 500000000)
        self.assertEqual(gcd(999999001, 999999002), 1)
        
        # Negative numbers
        self.assertEqual(gcd(-10, 5), 5)
        self.assertEqual(gcd(10, -5), 5)
        self.assertEqual(gcd(-10, -5), 5)
        
        # Coprime numbers
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(101, 103), 1)
        
        # Same numbers
        self.assertEqual(gcd(25, 25), 25)
        self.assertEqual(gcd(100, 100), 100)
        
        # One number is multiple of the other
        self.assertEqual(gcd(14, 7), 7)
        self.assertEqual(gcd(81, 9), 9)

    def test_chi_squared(self):
        text = "hello"
        expected_score = chi_squared(text)
        self.assertIsInstance(expected_score, float)

    def test_mod_inverse(self):
        self.assertEqual(mod_inverse(3, 11), 4)
        self.assertEqual(mod_inverse(10, 17), 12)
        self.assertIsNone(mod_inverse(2, 4))

    def test_text_clean(self):
        self.assertEqual(text_clean("Hello, World!"), "HELLOWORLD")
        self.assertEqual(text_clean("123"), "")

        # Teacher tests
        self.assertEqual(text_clean("hello"), "HELLO")
        self.assertEqual(text_clean('Hello, World!'), 'HELLOWORLD')
        self.assertEqual(text_clean('123ABC!@#def'), 'ABCDEF')
        self.assertEqual(text_clean('1234!@#$%^'), '')
        self.assertEqual(text_clean(''), '')
        self.assertEqual(text_clean('a1b2c3', LETTERS='0123456789'), '123')
        self.assertEqual(text_clean('hello', LETTERS='HELLO'), 'HELLO')
        self.assertEqual(text_clean('Hello, World!', LETTERS='HLWRD'), 'HLLWRLD')


    def test_text_block(self):
        self.assertEqual(text_block("HELLOWORLD", 5), "HELLO WORLD")
        self.assertEqual(text_block("ABCDE", 2), "AB CD E")

        # Teacher tests
        self.assertEqual(text_block('TESTMESSAGE'), 'TESTM ESSAG E')
        self.assertEqual(text_block('abcdefghijklmno', 4), 'abcd efgh ijkl mno')
        self.assertEqual(text_block('abcdefghi', 3), 'abc def ghi')
        self.assertEqual(text_block('abcdefghij', 2), 'ab cd ef gh ij')
        self.assertEqual(text_block('a', 3), 'a')
        self.assertEqual(text_block(''), '')
        self.assertEqual(text_block('abcdefgh', 8), 'abcdefgh')


if __name__ == '__main__':
    unittest.main()