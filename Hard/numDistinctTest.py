import unittest

from Hard.numDistinct import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        r = s.numDistinct("rabbbit", "rabbit")
        self.assertEqual(r, 3)
        r = s.numDistinct("babgbag", "bag")
        self.assertEqual(r, 5)


if __name__ == "__main__":
    unittest.main()
