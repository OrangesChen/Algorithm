from typing import List

# https://www.notion.so/354-058151dc067245e4a69c6f94e42e3768
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        # 排序
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # 计算套娃数量 储存到f中
        f = [1] * n
        for i in range(n):
            for j in range(i):
                # 数组已经排好序 只需要比较第二位大小即可
                if envelopes[j][1] < envelopes[i][1]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)
