from typing import List


class Solution:
    # 今天，书店老板有一家店打算试营业customers.length分钟。每分钟都有一些顾客（customers[i]）会进入书店，
    # 所有这些顾客都会在那一分钟结束后离开。
    # 在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
    # 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
    # 书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续X 分钟不生气，但却只能使用一次。
    # 请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
    # 示例：
    # 输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
    # 输出：16
    # 解释：
    # 书店老板在最后 3 分钟保持冷静。
    # 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
    #
    # https://www.notion.so/1052-f9816380b0ba42da83f9cfdd8e2d7684
    @staticmethod
    def maxSatisfied(customers: List[int], grumpy: List[int], x: int) -> int:
        n = len(customers)
        # 1 先计算顾客总数
        # 2 计算x分钟生气总数 保存最大值
        # 3 上一个如果为1 则减去顾客数量 下一个为1则加上顾客数量 时间复杂度O(n)
        sum_cache = 0
        total = 0
        pre_index = 0
        # 生气的总数最大
        max_sum = 0
        for i in range(n):
            if grumpy[i] == 0:
                total = total + customers[i]
            if i == 0:
                for j in range(x):
                    if (i + j) < n:
                        if grumpy[i + j] == 1:
                            max_sum += customers[i + j]
            else:
                if pre_index + x < n and grumpy[pre_index] == 1:
                    max_sum -= customers[pre_index]
                if pre_index + x < n and grumpy[pre_index + x] == 1:
                    max_sum += customers[pre_index + x]
                pre_index += 1
            if max_sum > sum_cache:
                sum_cache = max_sum
                index = i
        for j in range(x):
            if (index + j) < n:
                grumpy[index + j] = 0
        return total + sum_cache
