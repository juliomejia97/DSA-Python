class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            # Insert the data to the final of the linked list
            self.head.next = node
            self.head = node
        else:
            # Insert the data for a size of 0
            self.tail = node
            self.head = node
        self.count += 1

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            # The data of the current node found
            if current.data == data:
                # The first node is going to be delete
                if current == self.tail:
                    self.tail = current.next
                # Is not the first node
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next

    def size(self):
        return self.count

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False

    def clear(self):
        self.tail = None
        self.head = None
        self.count = 0


words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('cheese')
words.append('spam')
words.append('coke')

current = words.tail
print("The size of the list is: ", words.size())
for word in words.iter():
    print(word)
print("Delete process of cheese:")
words.delete('cheese')
print("The size of the list is: ", words.size())
print("Searching ---- spam", words.search('spam'))
print("Searching ---- spam", words.search('cheese'))
print("Clear the list, babe!")
words.clear()
print("The size of the list is: ", words.size())
