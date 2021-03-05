import unittest

from Hard.maxEnvelopes import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        # envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
        envelopes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [5, 5], [6, 7], [7, 8]]
        r = s.maxEnvelopes(envelopes)
        self.assertEqual(r, 7)

    def test_err(self):
        s = Solution()
        envelopes = [
            [15, 8],
            [2, 20],
            [2, 14],
            [4, 17],
            [8, 19],
            [8, 9],
            [5, 7],
            [11, 19],
            [8, 11],
            [13, 11],
            [2, 13],
            [11, 19],
            [8, 11],
            [13, 11],
            [2, 13],
            [11, 19],
            [16, 1],
            [18, 13],
            [14, 17],
            [18, 19],
        ]
        r = s.maxEnvelopes(envelopes)
        self.assertEqual(r, 5)


if __name__ == "__main__":
    unittest.main()
