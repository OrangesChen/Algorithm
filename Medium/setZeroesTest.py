import unittest

from Medium.setZeroes import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        s.setZeroes(matrix)
        self.assertEqual(matrix, [[1,0,1],[0,0,0],[1,0,1]])
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        s.setZeroes(matrix)
        self.assertEqual(matrix, [[0,0,0,0],[0,4,5,0],[0,3,1,0]])


if __name__ == '__main__':
    unittest.main()
