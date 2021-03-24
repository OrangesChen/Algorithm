from typing import List


# 456. 132 模式
# 给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列
# 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
#
# 如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
#
# 进阶：很容易想到时间复杂度为 O(n^2) 的解决方案，你可以设计一个时间复杂度为 O(n logn) 或 O(n) 的解决方案吗？
#
# 示例 1：
#
# 输入：nums = [1,2,3,4]
# 输出：false
# 解释：序列中不存在 132 模式的子序列。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/132-pattern

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 单调栈
        n = len(nums)
        left_min = [float("inf")] * n
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i - 1])
        stk = []
        for j in range(n - 1, -1, -1):
            numsk = float("-inf")
            while stk and stk[-1] < nums[j]:
                numsk = stk.pop()
            if left_min[j] < numsk:
                return True
            stk.append(nums[j])
        return False

