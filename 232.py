class MyQueue:
    '''
    使用两个栈实现队列
    '''
    
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []# 一个栈进行输入操作
        self.output = []# 一个栈进行输出操作，将输入栈中的元素反转
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while len(self.output) != 0:# 将输出栈中所有元素移存至输入栈中
            self.input.append(self.output.pop())
        self.input.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.input) != 0:# 将输入栈中所有数据移存至输出栈中
            self.output.append(self.input.pop())
        x = self.output.pop()            
        return x

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while len(self.input) != 0:# 将所有数据移存至输出栈中
            self.output.append(self.input.pop())
        x = self.output[-1]     
        return x
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        while len(self.input) != 0:# 将所有数据移存至输出栈中
            self.output.append(self.input.pop())
        if len(self.output) != 0:# 判断输出栈是否为空
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
