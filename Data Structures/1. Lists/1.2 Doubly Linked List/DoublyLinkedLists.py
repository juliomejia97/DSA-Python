class Node(object):
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList(object):

    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        new_node = Node(data, None, None)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def delete(self, data):
        current = self.head
        node_deleted = False
        # Case 1. There is no data
        if not current:
            node_deleted = False
        # Case 2. Data is at the begining
        elif current.data == data:
            self.head = self.head.next
            self.head.prev = None
            node_deleted = True
        # Case 3. Data is a the end
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        # Case 4. Data is somewhere at the middle of the list
        else:
            while current:
                if current.data == data:
                    # The prev node now ne
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
            current = current.next

        if node_deleted:
            self.count -= 1

    def iter(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def contains(self, data):
        for val in self.iter():
            if val == data:
                return True
        return False


words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('cheese')
words.append('spam')
words.append('coke')
print("------------ Before -----------")
for word in words.iter():
    print(word)
print("------------ Test Contains -----------")
print(words.contains('egg'))
words.delete('egg')
print(words.contains('egg'))
print(words.contains('bread'))
print("------------ After -----------")
for word in words.iter():
    print(word)
