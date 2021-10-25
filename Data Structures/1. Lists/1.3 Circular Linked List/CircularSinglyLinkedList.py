class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.tail.next = self.head
        self.count += 1

    def delete(self, data):
        current = self.head
        prev = self.head
        while prev == current or prev != self.tail:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                elif current == self.tail:
                    self.tail = prev
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next

    def iter(self):
        current = self.head
        prev = self.head
        while prev == current or prev != self.tail:
            value = current.data
            prev = current
            current = current.next
            yield value


words = CircularLinkedList()
words.append('egg')
words.append('ham')
words.append('cheese')
words.append('spam')
words.append('coke')

print("------ Before ------")
for word in words.iter():
    print(word)

words.delete('coke')

print("------ After ------")
for word in words.iter():
    print(word)
