# O(n)
# O(1)
class MaxStackEfficient:
    def __init__(self):
        self.mainStack = []
        self.maximum = -float('inf')

    def push(self, val):
        self.mainStack.append(val)
        self.maximum = max(self.maximum, val)

    def pop(self):
        value = self.mainStack.pop()
        if value == self.maximum:
            self.maximum = max(
                self.mainStack) if self.mainStack else -float('inf')

    def max(self):
        return self.maximum

# O(n)
# O(n)


class MaxStack:
    def __init__(self):
        self.mainStack = []
        self.cacheStack = []

    def push(self, val):
        self.mainStack.append(val)
        if(len(self.mainStack) == 1):
            self.cacheStack.append(val)
            return
        if val > self.cacheStack[-1]:
            self.cacheStack.append(val)
        else:
            maxValue = self.cacheStack[-1]
            self.cacheStack.append(maxValue)

    def pop(self):
        self.mainStack.pop()
        self.cacheStack.pop()

    def max(self):
        return self.cacheStack[-1]


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
