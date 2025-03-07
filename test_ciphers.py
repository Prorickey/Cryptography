import unittest
from ciphers import caesar

class TestUtilities(unittest.TestCase):
    def test_caesar(self):
        # Teacher tests
        self.assertEqual(caesar('HELLO', 3), 'KHOOR')
        self.assertEqual(caesar('KHOOR', 3, decrypt=True), 'hello')
        self.assertEqual(caesar('XYZ', 3), 'ABC')
        self.assertEqual(caesar('ABC', 3, decrypt=True), 'xyz')
        self.assertEqual(caesar('Hello, World!', 5), 'MJQQT BTWQI')
        self.assertEqual(caesar('MJQQT BTWQI', 5, decrypt=True), 'helloworld')
        self.assertEqual(caesar('HELLO', -3), 'EBIIL')
        self.assertEqual(caesar('EBIIL', -3, decrypt=True), 'hello')
        self.assertEqual(caesar('HELLO', 0), 'HELLO')
        self.assertEqual(caesar('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3), 'DEFGH IJKLM NOPQR STUVW XYZAB C')
        self.assertEqual(caesar('HELLO', 0, decrypt=True), 'hello')
        self.assertEqual(caesar('DEFGH IJKLM NOPQR STUVW XYZAB C', 3, decrypt=True), 'abcdefghijklmnopqrstuvwxyz')

if __name__ == '__main__':
    unittest.main()