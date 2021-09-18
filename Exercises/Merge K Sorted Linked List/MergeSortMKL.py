from typing import List


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    mid = len(lists)//2
    left = mergeKLists(lists[:mid])
    rigth = mergeKLists(lists[mid:])
    return mergeList(left, rigth)


def mergeList(l, r):
    head = dummy = ListNode(0)
    while l and r:
        if l.val <= r.val:
            dummy.next = ListNode(l.val)
            dummy = dummy.next
            l = l.next
        elif l.val > r.val:
            dummy.next = ListNode(r.val)
            dummy = dummy.next
            r = r.next
    # Add the other parts that are missing
    if l:
        dummy.next = l
    if r:
        dummy.next = r
    return head.next


a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))
print(mergeKLists([a, b, c]))
