# 59. 螺旋矩阵 II
# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left, right, up, down = 0, n - 1, 0, n - 1
        cur_d = 0
        # 移动方向
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_val = 1
        x, y = 0, 0
        while cur_val <= n * n:
            res[x][y] = cur_val
            if cur_d == 0 and y == right:
                cur_d += 1
                up += 1
            elif cur_d == 1 and x == down:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                down -= 1
            elif cur_d == 3 and x == up:
                cur_d += 1
                left += 1
            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
            cur_val += 1
        return res
