import unittest

from Medium.reverseBetween import Solution, ListNode


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        head = [1, 2, 3, 4, 5]
        left = 2
        right = 4
        root = ListNode(-1)
        next = root
        for i in head:
            node = ListNode(i)
            next.next = node
            next = next.next
        r = s.reverseBetween(root.next, left, right)
        cur = r
        ans = []
        while cur:
            ans.append(cur.val)
            cur = cur.next
        self.assertEqual(ans, [1, 4, 3, 2, 5])
        left = 1
        right = 1
        r = s.reverseBetween(ListNode(5), left, right)
        cur = r
        ans = []
        while cur:
            ans.append(cur.val)
            cur = cur.next
        self.assertEqual(ans, [5])

    def test_reverse(self):
        s = Solution()
        root = ListNode(-1)
        next = root
        head = [1, 2, 3, 4, 5]
        for i in head:
            node = ListNode(i)
            next.next = node
            next = next.next
        r = s.reverseList(root.next)
        cur = r
        ans = []
        while cur:
            ans.append(cur.val)
            cur = cur.next
        self.assertEqual(ans, [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
