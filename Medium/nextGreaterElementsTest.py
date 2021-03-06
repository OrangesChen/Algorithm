import unittest

from Medium.nextGreaterElements import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        nums = [1, 5, 3, 6, 8]
        r = s.nextGreaterElements(nums)
        self.assertEqual(r, [5, 6, 6, 8, -1])

    def test_next(self):
        s = Solution()
        nums = [1, 2, 3, 4, 3]
        r = s.nextGreaterElements(nums)
        self.assertEqual(r, [2, 3, 4, -1, 4])

    def test_searchBinary(self):
        s = Solution()
        nums = [1, 2, 3, 4, 5, 6]
        r = s.searchBin(nums, 1)
        self.assertEqual(r, 0)


if __name__ == "__main__":
    unittest.main()
