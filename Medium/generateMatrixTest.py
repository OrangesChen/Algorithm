import unittest

from Medium.generateMatrix import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        r = s.generateMatrix(3)
        self.assertEqual(r, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
        r = s.generateMatrix(1)
        self.assertEqual(r, [[1]])


if __name__ == "__main__":
    unittest.main()
