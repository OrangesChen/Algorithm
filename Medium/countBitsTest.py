import unittest

from Medium.countBits import Solution


class CountBitsTest(unittest.TestCase):
    def test_example(self):
        s = Solution()
        r = s.countBits(2)
        self.assertEqual(r, [0, 1, 1])


if __name__ == "__main__":
    unittest.main()
