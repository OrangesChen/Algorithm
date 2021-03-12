# 331. 验证二叉树的前序序列化
# 序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# 例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
# 给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
# 每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
# 你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如"1,,3" 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # 根如果后面有数据 必须要有两个数值
        # # 后面则为最后的节点
        # 左节点 右节点 左子树是否有效 右子树是否有效 根节点-左子树-右子数 是否有效
        # 树至少有3个节点
        # 栈 - 入度出度
        stk = []
        for node in preorder.split(","):
            stk.append(node)
            while len(stk) >= 3 and stk[-1] == stk[-2] == "#" and stk[-3] != "#":
                stk.pop(), stk.pop(), stk.pop()
                stk.append("#")
        return len(stk) == 1 and stk.pop() == "#"
