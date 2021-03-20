import unittest

from Medium.evalRPN import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(s.evalRPN(tokens), 9)
        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(s.evalRPN(tokens), 6)
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(s.evalRPN(tokens), 22)


if __name__ == '__main__':
    unittest.main()
