class Solution:
    # https://www.notion.so/338-ae975cfca22c4a00b0ddc986d0f2ac74
    @staticmethod
    def countBits(num):
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
