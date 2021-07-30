# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        carry = 0
        sum = 0
        l3 = ListNode(-1)
        result = l3
        while l1 or l2 or carry != 0:
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            sum = x + y + carry
            carry = sum//10
            l3.next = ListNode(sum % 10)
            l3 = l3.next
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        return result.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
print()
