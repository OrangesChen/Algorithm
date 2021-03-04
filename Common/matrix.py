from typing import List


class MatrixSolution:
    # 数组形式的整数加法
    # 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。
    # 例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
    # 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
    # 输入：A = [1,2,0,0], K = 34
    # 输出：[1,2,3,4]
    # 解释：1200 + 34 = 1234
    @staticmethod
    def addToArrayForm(A: List[int], K: int) -> List[int]:
        # 投机取巧
        # return list(map(int, str(int(''.join(map(str, A))) + K)))
        # 首位数组 长度小于K 需要新增0 循环替换为K
        i = len(A) - 1
        while K:
            # 数组末位加K [1, 2, 0, 34]
            A[i] += K
            # K = 3 A = [1, 2, 0, 4]
            K, A[i] = A[i] // 10, A[i] % 10
            i -= 1
            # 新增的K 导致数组数量添加 头部新增数字
            if i < 0 and K:
                A.insert(0, 0)
                i = 0
        return A

    # 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
    # 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵
    # 链接：[https://leetcode-cn.com/problems/toeplitz-matrix](https://leetcode-cn.com/problems/toeplitz-matrix)

    #
    # *解题思路： 傻瓜式解决方案
    #  1 检测水平对角线对比
    #  2 检测垂直对角线对比
    #  解法1：遍历矩阵和左上角的元素进行比较即可
    #  解法2：对角线下标差值一致，可通过记录差值的方式进行判断
    # 在 Python 代码中用切片操作，第 ii 行的 [0, N - 2][0,N−2]的切片等于第 i + 1 i+1 行的 [1, N - 1][1,N−1]，这样能节省代码长度。
    @staticmethod
    def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True

    # 给你一个二维整数数组 `matrix`， 返回 `matrix` 的 **转置矩阵** 。
    # 矩阵的 **转置** 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
    # 初始化为0的倒置矩阵与原来的下标替换
    @staticmethod
    def transpose(matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        temp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                temp[i][j] = matrix[j][i]
        return temp
