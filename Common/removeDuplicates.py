# 1047 删除字符串中的所有相邻重复项
# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string


class Solution:
    def removeDuplicates(self, S: str) -> str:
        # 使用栈进行操作
        ret = []
        for c in S:
            if ret and ret[-1] == c:
                ret.pop()
            else:
                ret.append(c)
        return "".join(ret)
