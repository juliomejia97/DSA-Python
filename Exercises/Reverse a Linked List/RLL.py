from typing import List
from collections import deque


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)
        # Iterative Solution

    def reverseIteratively(self, head):
        st = deque()
        temp = ListNode(-1)
        res = temp
        while head:
            st.append(head.val)
            head = head.next
        while len(st) > 0:
            value = st.pop()
            temp.next = ListNode(value)
            temp = temp.next
        return res.next
        # Recursive Solution

    def reverseRecursively(self, head):
        if head == None or head.next == None:
            return head
        ll = self.reverseRecursively(head.next)
        head.next.next = head
        head.next = None
        return ll

        # Test Program
        # Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
res = testHead.reverseRecursively(testHead)
# testHead.reverseRecursively(testHead)
print("List after reversal: ")
res.printList()
# 0 1 2 3 4
