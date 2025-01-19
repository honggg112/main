class MinStack:
    def __init__(self):
        self.stack = []          # 主栈
        self.min_stack = []      # 辅助栈，用来保存每个状态下的最小值

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:  # 如果主栈非空才执行pop
            top = self.stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None  # 栈为空时返回None

min_stack = MinStack()
while True:
    try:
        command = input().strip()
        if command.startswith('push'):
            value = int(command.split()[1])
            min_stack.push(value)
        elif command.startswith('pop'):
            min_stack.pop()  # 空栈时不进行任何操作
        elif command.startswith('min'):
            min_value = min_stack.min()
            if min_value is not None:
                print(min_value)  # 只有在栈非空时才打印最小值
    except EOFError:
        break