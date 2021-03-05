from typing import List

# https://www.notion.so/354-058151dc067245e4a69c6f94e42e3768
# 354 禁止套娃
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式(w, h)出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 说明:
# 不允许旋转信封。
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
