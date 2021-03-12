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

    def test_cal2(self):
        s = Solution()
        r = s.calculate2("14/3*2")
        self.assertEqual(r, 8)
        # r = s.calculate2(" 3/2 ")
        # self.assertEqual(r, 1)
        # r = s.calculate2(" 3+5 / 2 ")
        # self.assertEqual(r, 5)
        # r = s.calculate2("1")
        # self.assertEqual(r, 1)
        # r = s.calculate2("0-2147483647")
        # self.assertEqual(r, -2147483647)


if __name__ == "__main__":
    unittest.main()
