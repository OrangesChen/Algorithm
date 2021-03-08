import unittest

from Hard.partition import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        # r = s.partition('aab')
        # self.assertEqual(r, [['a', 'a', 'b'], ['aa', 'b']])
        r = s.minCut("aab")
        self.assertEqual(r, 1)


if __name__ == "__main__":
    unittest.main()
