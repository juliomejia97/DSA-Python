class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.visited = False

    def prettyPrint(self):
        c = self
        while c:
            print(c.val, end="\t")
            c = c.next
        print('\n')


def intersection(a, b):
    # Visit the first Linked List
    while a:
        a.visited = True
        a = a.next
    # Visit the second and where I found
    # The first True, return the node
    while b:
        if b.visited:
            return b
        b = b.next


def intersectionSet(a, b):
    c1 = set()
    while a:
        c1.add(a)
        a = a.next
    while b:
        if b in c1:
            return b
        b = b.next
    return None


def intersectionCount(a, b):
    head1Aux = a
    c1 = 0
    while a:
        c1 += 1
        a = a.next
    head2Aux = b
    c2 = 0
    while b:
        c2 += 1
        b = b.next
    dif = abs(c1-c2)
    if c1 > c2:
        while dif > 0:
            head1Aux = head1Aux.next
            dif -= 1
    else:
        while dif > 0:
            head2Aux = head2Aux.next
            dif -= 1
    while head1Aux and head2Aux:
        if head1Aux == head2Aux:
            return head1Aux
        head1Aux = head1Aux.next
        head2Aux = head2Aux.next
    return -1


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersectionCount(a, b)
c.prettyPrint()
