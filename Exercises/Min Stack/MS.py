class minStack(object):
    def __init__(self):
        self.mainStack = []
        self.minValue = float('inf')

    def push(self, x):
        self.mainStack.append(x)
        self.minValue = min(self.minValue, x)

    def pop(self):
        value = self.mainStack.pop()
        if value == self.minValue:
            self.minValue = min(
                self.mainStack) if self.mainStack else float('inf')

    def top(self):
        return self.mainStack[-1]

    def getMin(self):
        return self.minValue


x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
