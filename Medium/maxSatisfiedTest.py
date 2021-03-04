import unittest

from Medium.maxSatisfied import Solution


class MaxSatisfiedTest(unittest.TestCase):
    def test_example(self):
        s = Solution()
        customers = [1, 0, 1, 2, 1, 1, 7, 5]
        grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
        X = 3
        r = s.maxSatisfied(customers, grumpy, X)
        self.assertEqual(r, 16)


if __name__ == '__main__':
    unittest.main()
