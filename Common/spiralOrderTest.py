import unittest

from Common.spiralOrder import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        r = s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(r, [1, 2, 3, 6, 9, 8, 7, 4, 5])
        r = s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        self.assertEqual(r, [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
