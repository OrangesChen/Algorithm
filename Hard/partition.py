# 131、132 分割回文串
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 回文串 是正着读和反着读都一样的字符串。
# https://leetcode-cn.com/problems/palindrome-partitioning/

# 回溯法： 是一种算法思想，而递归是一种编程方法，回溯可以用递归来实现
class Solution:
    # 判断字符串是否为回文
    def is_palindrome(self, p):
        return p == p[::-1]

    def partition(self, s):
        # self.isPalindrome = lambda s: s == s[::-1]
        res = []
        self.backtrack(s, res, [])
        return res

    def backtrack(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            r = self.is_palindrome(s[:i])
            if r:
                self.backtrack(s[i:], res, path + [s[:i]])

    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [n] * n
        for i in range(n):
            if self.is_palindrome(s[0: i + 1]):
                dp[i] = 0
                continue
            for j in range(i):
                if self.is_palindrome(s[j + 1: i + 1]):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]
