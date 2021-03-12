import unittest

from Medium.isValidSerialization import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        r = s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
        self.assertEqual(r, True)
        r = s.isValidSerialization("1,#")
        self.assertEqual(r, False)
        r = s.isValidSerialization("9,#,#,1")
        self.assertEqual(r, False)
        r = s.isValidSerialization("1,#,#,#,#")
        self.assertEqual(r, False)


if __name__ == "__main__":
    unittest.main()
