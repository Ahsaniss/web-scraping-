import unittest

import test_main
from Prime_num_finder import is_prime
#inhertence use ( )
class MyTestCase(unittest.TestCase):

    def test_prime(self):
        """Test if prime numbers return True."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

    def test_not_prime(self):
        """Test if non-prime numbers return False."""
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(1))

    def test_edge_cases(self):
        """Test the edge cases for prime number checks."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-5))

    def test_Equal_cases(self):

        self.assertEqual(is_prime(2),True)
        self.assertEqual(is_prime(4),False)
        self.assertEqual(is_prime(11),True)
        self.assertEqual(is_prime(15),False)

    def test_NotEqual_cases(self):
        self.assertNotEqual(is_prime(4),True)
        self.assertNotEqual(is_prime(5), False)

    def test_is_cases(self):
        self.assertIs(is_prime(2), True)
        self.assertIs(is_prime(4), False)
if __name__ == "__main__":
    unittest.main()
