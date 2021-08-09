class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.value)
            current_node = current_node.next
        return str(result)


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    i = 0
    h1 = head
    h2 = head
    while i < n:
        if(h2.next == None):
            if(i == n-1):
                head = head.next
            return head
        i += 1
        h2 = h2.next
    while h2.next != None:
        h2 = h2.next
        h1 = h1.next
    h1.next = h1.next.next
    return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = removeNthFromEnd(head, 1)
print(head)
# [1, 2, 4, 5]
