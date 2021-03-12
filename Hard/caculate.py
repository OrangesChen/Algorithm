# 224.基本计算器
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
# 提示：
#
# 1 <= s.length <= 3 * 105
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式

# https://leetcode-cn.com/problems/basic-calculator/


class Solution:
    # def operation(self, a: str, o: str, b: str):
    #     if o == '-':
    #         return str(int(b) - int(a))
    #     if o == '+':
    #         return str(int(b) + int(a))
    #
    # def calculate(self, s: str) -> int:
    #     # 只有加减方法和括号 括号优先计算 使用栈计算 存在负数 需要判断负数存在 括号左侧和第一位数字可能是负数
    #     # 不管+还是- 都保存为数字 所有运算都是加法
    # emmm 以下是我的暴力解决方法 又臭又长的代码 主要还是为了编译能过去hhhh 不管怎样我成功了！！！
    #     stk = []
    #     # 如果只是数字 则直接输出
    #     if s.count('-') == 0 and s.count('+') == 0 and s.count('(') == 0:
    #         return int(s)
    #     # 删除空格
    #     s = ''.join(s.split())
    #     # 标记栈里面是否存在括号
    #     flag = 0
    #     is_negative = False
    #     pre = ''
    #     idx = 0
    #     for ch in s:
    #         if ch == '(':
    #             stk.append(ch)
    #             flag += 1
    #             if pre == '-':
    #                 is_negative = True
    #                 pre = ''
    #         else:
    #             if flag == 0:
    #                 if len(stk) == 0:
    #                     if ch == '-':
    #                         pre = ch
    #                     else:
    #                         if s[idx + 1] == '+' or s[idx + 1] == '-' or s[idx+1] == ')':
    #                             stk.append(pre + ch)
    #                             pre = ''
    #                         else:
    #                             pre = pre + ch
    #                 elif stk[-1] == '+' or stk[-1] == '-':
    #                     if idx == len(s) - 1 or s[idx + 1] == '+' or s[idx + 1] == '-':
    #                         ret = self.operation(pre+ch, stk.pop(), stk.pop())
    #                         stk.append(ret)
    #                         pre = ''
    #                     else:
    #                         pre = pre + ch
    #                 else:
    #                     stk.append(pre+ch)
    #                     pre = ''
    #             else:
    #                 if ch == ')':
    #                     ret = stk.pop()
    #                     while stk[-1] != '(':
    #                         ret = self.operation(ret, stk.pop(), stk.pop())
    #                     stk.pop()
    #                     flag -= 1
    #                     if len(stk) != 0:
    #                         if stk[-1] == '+' or stk[-1] == '-':
    #                             ret = self.operation(ret, stk.pop(), stk.pop())
    #                     stk.append(ret)
    #                 elif stk[-1] == '(':
    #                     if ch == '-':
    #                         pre = '-'
    #                     else:
    #                         if s[idx+1] == '+' or s[idx+1] == '-' or s[idx+1] == ')':
    #                             stk.append(pre+ch)
    #                             pre = ''
    #                         else:
    #                             pre = pre + ch
    #                 else:
    #                     if stk[-1] == '+' or stk[-1] == '-':
    #                         if s[idx + 1] == '+' or s[idx + 1] == '-' or s[idx + 1] == ')':
    #                             ret = self.operation(pre + ch, stk.pop(), stk.pop())
    #                             pre = ''
    #                             stk.append(ret)
    #                         else:
    #                             pre = pre + ch
    #                     else:
    #                         stk.append(pre + ch)
    #                         pre = ''
    #         idx += 1
    #     if is_negative:
    #         pre = '-'
    #     return int(pre + stk.pop())

    def calculate(self, s):
        res, num, sign = 0, 0, 1
        stk = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stk.append(res)
                stk.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                # 正负数
                res *= stk.pop()
                # 字符相加
                res += stk.pop()
        res += sign * num
        return res

    # 227.基本计算器 II
    # 示例 1：
    #
    # 输入：s = "3+2*2"
    # 输出：7
    # 示例 2：
    #
    # 输入：s = " 3/2 "
    # 输出：1
    # 示例 3：
    #
    # 输入：s = " 3+5 / 2 "
    # 输出：5
    #
    # 来源：力扣（LeetCode）
    # 链接：https://leetcode-cn.com/problems/basic-calculator-ii
    # 1 先计算* / 法 最后再算加减法

    def operation(self, operation, a, b):
        if operation == "/":
            return int(a / b)
        elif operation == "*":
            return a * b

    # 227. 基本计算器 II
    def calculate2(self, s: str) -> int:
        num, res, operation, sign = 0, 0, None, 1
        stk = []
        for ch in s:
            if ch.isdigit():
                num = 10 * num + int(ch)
            elif ch == "+" or ch == "-":
                if operation:
                    res = self.operation(operation, stk.pop(), num)
                    stk.append(res)
                    operation = None
                else:
                    res += sign * num
                    stk.append(res)
                num = 0
                res = 0
                sign = 1 if ch == "+" else -1
            elif ch == "/" or ch == "*":
                if operation:
                    res = self.operation(operation, stk.pop(), num)
                else:
                    res += sign * num
                stk.append(res)
                operation = ch
                num = 0
                res = 0
                sign = 1
        # 将栈中最后一位数据加入
        if operation:
            res = self.operation(operation, stk.pop(), num)
            stk.append(res)
        else:
            res = num * sign
            stk.append(res)
        return sum(stk)
