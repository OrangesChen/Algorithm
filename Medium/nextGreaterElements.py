# # 503 下一个更大元素
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/next-greater-element-ii
# https://www.notion.so/503-II-fa7d7d7a54d741fa82b9bc15bde24c02
from typing import List


class Solution:
    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
    #     # 暴力求解 循环搜索是否存在下一个更大的元素 应该会超出时间限制
    #     # 数组是无序的 无法知道从头循环是否存在下一个最大的数字（暂存最大值 可以先比较是否小于最大值 如果小于则循环查找）
    #     m = len(nums)
    #     res = [0] * m
    #     pre_next = 0
    #     for i in range(m):
    #         flag = 0
    #         if i > 0:
    #             if pre_next < nums[i]:
    #                 pre_next = nums[i]
    #         for j in range(i, m):
    #             if nums[i] < nums[j]:
    #                 res[i] = nums[j]
    #                 flag = 1
    #                 break
    #         if flag == 0:
    #             if nums[i] > pre_next:
    #                 res[i] = -1
    #                 flag = 1
    #             else:
    #                 for k in range(i):
    #                     if nums[i] < nums[k]:
    #                         res[i] = nums[k]
    #                         flag = 1
    #                         break
    #         if flag == 0:
    #             res[i] = -1
    #     return res

    # 单调栈 单调栈中保存下标 从栈底部到栈顶的下标在数组对应的值是单调不升的
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = list()
        for i in range(n * 2 - 1):
            # 比较栈顶元素 stack[-1] 下标 i % n
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
            print(stack)
            print(res)
        return res

    # 二分查找 已排序数组
    def searchBin(self, nums: List[int], x: int):
        return self.findBinary(nums, x, 0, len(nums) - 1)

    def findBinary(self, nums: List[int], x: int, left: int, right: int) -> int:
        if left > right:
            return -1
        mid = int((right - left) / 2) + left
        if x == nums[mid]:
            return mid
        else:
            if x < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            return self.findBinary(nums, x, left, right)
