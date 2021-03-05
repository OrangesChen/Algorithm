from typing import List


# 304 二维区域和检索-矩阵不可变
# https://www.notion.so/304-a7bb202feff84a0abc7828208f3ed7e6
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            M, N = 0, 0
        else:
            M, N = len(matrix), len(matrix[0])
        self.preSum = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                self.preSum[i + 1][j + 1] = (
                    self.preSum[i][j + 1]
                    + self.preSum[i + 1][j]
                    - self.preSum[i][j]
                    + matrix[i][j]
                )

    # 时间复杂度：构造函数的时间复杂度是 O(M * N)O(M∗N)； sumRegion 函数的时间复杂度是 O(1)O(1)
    # 空间复杂度：利用了preSum 矩阵，空间是 O(M * N)O(M∗N)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.preSum[row2 + 1][col2 + 1]
            - self.preSum[row2 + 1][col1]
            - self.preSum[row1][col2 + 1]
            + self.preSum[row1][col1]
        )
