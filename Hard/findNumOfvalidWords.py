# https://www.notion.so/1178-93d7d87acbf34ca6b88a0cefd0b4c2da
# 1178 猜字谜

# 开始计算这个puzzle有多少可行的word
# 因为puzzle的首字母一定要有，所以我们把首字母拿出来，最后再处理
# 此处举例 puzzle = "abslute"
# 那么我们需要做的就是 枚举 “bslute” 所有可能的组合（长度1-6都要枚举，每次枚举的结果都要加上首字母“a”）
# 难点就是枚举的 长度 任意，选择的位置也任意，比如加上首字母后 {“a”,"b"}、{"a"}、{"a","u","l","s"}都是合法结果
# 那么这个 choose 变量就是做这个事情的
# choose利用二进制的性质，起到了一个“选择”的作用，choose二进制从右向左数，如果这一位为 1，侧表示要从“bslute”选出这一位
# choose就是一个选择过滤窗
# “bslute” index是从左向右，而二进制表示的 mask和 choose 都是从右向左数的
# 举例
# for choose in range(1 << 6)
# choose 从 0 开始 到（不包含64）结束
# choose = 0时：
# choose从右向左的位次（从右向左）    6543210
# choose的二进制表示             0b0000000
# 如果choose的第i位（从右向左数<--）为1，表示选择 出来 “bslute”的第i位（从左向右数-->）
# 下面开始遍历 “bslute”

# 以下代码的含义解释为：
#                 for i in range(6):
#                     if choose & (1 << i):
# i代表了“bslute”  从左向右 数第i位
# i同时代表了choose 从右向左 数第i位
# if choose & (1 << i) 表示 如果当前choose位为1
# 每一次新的choose（新的组合），都通过遍历“bslute”把相对应的位选出来
# 因为二进制巧妙的性质，choose从0到63就是从这6位中 依次选出 所有的组合
# 举例
# choose = 0时：
# choose从右向左的位次（从右向左）     543210
# choose的二进制表示             0b0000000
# “bslute”的组合选择情况            ------
# “bslute”的对应 index            543210 (从右向左)
# “bslute”对应的位置               etulsb
# 结果：全不选，因为choose全是0
# 加上首字母“a”的人类便于理解结果含义 {“a”}(我们没有在代码里面实际做这个东西)
# mask按照构造 word 的 mask 的相同想法去构造，结果就是 key = 1（含义 key = {“a”}）

# choose = 1时：
# choose从右向左的位次（从右向左）     543210
# choose的二进制表示             0b0000001
# “bslute”的组合选择情况            -----b
# “bslute”的对应 index            543210 (从右向左)
# “bslute”对应的位置               etulsb
# 结果：选"b"，因为choose对应位是1
# 加上首字母“a”的人类便于理解结果含义 {“a”,"b"}(我们没有在代码里面实际做这个东西)
# mask按照构造 word 的 mask 的相同想法去构造，结果就是 key = 3 = 0b11（含义 key = {“a”,"b"}）

# 过了几轮.......

# choose = 6时：
# choose从右向左的位次（从右向左）     543210
# choose的二进制表示             0b0000110
# “bslute”的组合选择情况            ---ls-
# “bslute”的对应 index            543210 (从右向左)
# “bslute”对应的位置               etulsb
# 结果：选"l"和“s”，因为choose对应位是1
# 加上首字母“a”的人类便于理解结果含义 {“a”,"l","s"}(我们没有在代码里面实际做这个东西)
# mask按照构造 word 的 mask 的相同想法去构造，结果就是 key = 264193 （含义 key = {“a”,"l","s"}）

# 又过了好多轮

# 最后一轮
# choose = 63时：
# choose从右向左的位次（从右向左）     543210
# choose的二进制表示             0b0111111
# “bslute”的组合选择情况            etulsb
# “bslute”的对应 index            543210 (从右向左)
# “bslute”对应的位置               etulsb
# 结果：全选，因为choose全是1
# 加上首字母“a”的人类便于理解结果含义 {“a”,“b“,"s","l","u","t","e”}(我们没有在代码里面实际做这个东西)
# mask按照构造 word 的 mask 的相同想法去构造，结果就是 key = 1837075 （含义 key = {“a”,“b“,"s","l","u","t","e”}）
import collections
from typing import List


class Solution:
    @staticmethod
    def findNumOfValidWords(words: List[str], puzzles: List[str]) -> List[int]:
        frequency = collections.Counter()
        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord("a")))
            if str(bin(mask)).count("1") <= 7:
                frequency[mask] += 1

        ans = list()
        for puzzle in puzzles:
            total = 0

            # 枚举子集方法一
            # for choose in range(1 << 6):
            #     mask = 0
            #     for i in range(6):
            #         if choose & (1 << i):
            #             mask |= (1 << (ord(puzzle[i + 1]) - ord("a")))
            #     mask |= (1 << (ord(puzzle[0]) - ord("a")))
            #     if mask in frequency:
            #         total += frequency[mask]

            # 枚举子集方法二
            mask = 0
            for i in range(1, 7):
                mask |= (1 << (ord(puzzle[i]) - ord("a")))

            subset = mask
            while subset:
                s = subset | (1 << (ord(puzzle[0]) - ord("a")))
                if s in frequency:
                    total += frequency[s]
                subset = (subset - 1) & mask

            # 在枚举子集的过程中，要么会漏掉全集 mask，要么会漏掉空集
            # 这里会漏掉空集，因此需要额外判断空集
            if (1 << (ord(puzzle[0]) - ord("a"))) in frequency:
                total += frequency[1 << (ord(puzzle[0]) - ord("a"))]
            ans.append(total)
        return ans
