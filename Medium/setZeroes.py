# 73. 矩阵置零
# 给定一个m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#
# 进阶：
#
# 一个直观的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m+n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/set-matrix-zeroes
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        M, N = len(matrix), len(matrix[0])
        row, col = set(), set()
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(M):
            for j in range(N):
                if i in row or j in col:
                    matrix[i][j] = 0
