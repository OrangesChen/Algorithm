import unittest

from Common.myQueue import MyQueue


class MyTestCase(unittest.TestCase):
    def test_pop(self):
        s = MyQueue()
        s.push(1)
        s.push(3)
        r = s.pop()
        self.assertEqual(r, 1)

    def test_peek(self):
        s = MyQueue()
        s.push(1)
        s.push(3)
        r = s.peek()
        self.assertEqual(r, 1)

    def test_empty(self):
        s = MyQueue()
        s.push(1)
        r = s.empty()
        self.assertEqual(r, False)
        r = s.pop()
        self.assertEqual(r, True)


if __name__ == "__main__":
    unittest.main()
