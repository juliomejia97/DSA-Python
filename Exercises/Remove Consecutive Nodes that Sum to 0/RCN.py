class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = None


def removeZeroSumSublists(head: Node):
    dic = {}
    dummyNode = Node(0)
    dummyNode.next = head
    dic[0] = dummyNode
    cumS = 0
    while head:
        cumS += head.value
        if cumS in dic:
            # DELETE the others sums
            headAux = dic[cumS].next
            sumAux = cumS
            while headAux != head:
                sumAux += headAux.value
                del dic[sumAux]
                headAux = headAux.next
            dic[cumS].next = head.next
        else:
            dic[cumS] = head
        head = head.next
    return dic[0].next


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeZeroSumSublists(node)
while node:
    print(node.value, end=", ")
    node = node.next
print('\n')
