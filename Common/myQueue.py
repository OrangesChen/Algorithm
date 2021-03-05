# 232 用栈实现队列
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
#
# 实现 MyQueue 类：
#
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
# https://www.notion.so/232-c444d2a6dd8a44f7bb38f1300e6331b5


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.leftStack = []
        self.rightStack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # b中元素保持先进先出
        # 将b中的数据捣腾到栈a中去 此时a中的数据被还原为后进先出
        # 再将新元素插入a中 此时依然为后进先出顺序
        # 将a中的元素倒腾到b中 此时b中顺序变为先进先出
        while self.rightStack:
            self.leftStack.append(self.rightStack.pop())
        self.leftStack.append(x)
        while self.leftStack:
            self.rightStack.append(self.leftStack.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.rightStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.rightStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.rightStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
