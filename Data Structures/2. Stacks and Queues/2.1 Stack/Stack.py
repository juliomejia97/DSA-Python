class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
    def __str__(self) -> str:
        return str(self.data)
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
    def push(self,data):
        element = Node(data)
        if not self.top:
            self.top = element
        else:
            element.next = self.top
            self.top = element
        self.count += 1
    def pop(self):
        element = None
        if self.top:
            element =  self.top
            if element.next:
                self.top = element.next
                element.next = None
            else:
                self.top = None
            self.count -= 1
        return element
    def peek(self):
        if self.top:
            return self.top
        else:
            return None