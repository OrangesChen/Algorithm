from typing import List


# 150. 逆波兰表达式求值
# 根据 逆波兰表示法，求表达式的值。
#
# 有效的算符包括+、-、*、/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 说明：
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation

# 使用栈执行 leetcode上解题思路已经说的很明白啦哈哈
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for val in tokens:
            if (val.startswith('-') and val[1:] or val).isdigit():
                stk.append(int(val))
            else:
                num2 = stk.pop()
                num1 = stk.pop()
                if val == '+':
                    stk.append(num1 + num2)
                elif val == '-':
                    stk.append(num1 - num2)
                elif val == '/':
                    stk.append(int(num1 / num2))
                elif val == '*':
                    stk.append(num1 * num2)
        return stk.pop()
