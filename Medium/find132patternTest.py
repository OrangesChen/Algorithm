import unittest

from Medium.find132pattern import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        r = s.find132pattern([1, 2, 3, 4])
        self.assertEqual(r, False)
        r = s.find132pattern([3, 1, 4, 2])
        self.assertEqual(r, True)
        r = s.find132pattern([-1, 3, 2, 0])
        self.assertEqual(r, True)
        r = s.find132pattern([1, -4, 2, -1, 3, -3, -4, 0, -3, -1])
        self.assertEqual(r, True)


if __name__ == '__main__':
    unittest.main()
