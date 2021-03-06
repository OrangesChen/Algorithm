import unittest

from Medium.numMatrix import NumMatrix


class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
        s = NumMatrix(matrix)
        r = s.sumRegion(2, 1, 4, 3)
        self.assertEqual(r, 8)


if __name__ == "__main__":
    unittest.main()
