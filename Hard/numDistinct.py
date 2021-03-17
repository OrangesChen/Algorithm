# 115. 不同的子序列
# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE"是"ABCDE"的一个子序列，而"AEC"不是）
# 题目数据保证答案符合 32 位带符号整数范围
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/distinct-subsequences
# 示例1：
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 1 t 是 s 的子序列 t的长度小于s的长度
        # 动态规划
        # t[i] == s[j] dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
        # t[i] != s[j] dp[i][j] = dp[i+1][j]
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 当 j = n 时， t[j:]为空字符串，是任何子字符串的子序列，因此dp[i][n] = 1
        for i in range(m + 1):
            dp[i][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]
