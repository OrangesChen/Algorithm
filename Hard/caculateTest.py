import unittest

from Hard.caculate import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        r = s.calculate("(2)")
        self.assertEqual(r, 2)

    def test_multi_cal(self):
        s = Solution()
        r = s.calculate("1-11")
        self.assertEqual(r, -10)
        r = s.calculate("(1+(4+5+2)-3)+(6+8)")
        self.assertEqual(r, 23)

    def test_num_cal(self):
        s = Solution()
        r = s.calculate("2147483647")
        self.assertEqual(r, 2147483647)

    # 负数测试
    def test_negative_num(self):
        s = Solution()
        r = s.calculate("2-4-(8+2-6+(8+4-(1)+8-10))")
        self.assertEqual(r, -15)


if __name__ == "__main__":
    unittest.main()
