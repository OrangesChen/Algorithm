import unittest

from Common.removeDuplicates import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        r = s.removeDuplicates("abbaca")
        self.assertEqual(r, "ca")


if __name__ == "__main__":
    unittest.main()
