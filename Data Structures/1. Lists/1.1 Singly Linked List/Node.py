class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def invertList(l: Node) -> Node:
    if l.next == None:
        return l
    else:
        swap = invertList(l.next)
        # Move to the final
        l.next.next = l
        # The first index always have to point to the end
        l.next = None
        return swap


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)


n1.next = n2
n2.next = n3

result = invertList(n1)
while result:
    print(result.data)
    result = result.next
