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

# Complexity Analysis


def mergeKLists(lists: list[ListNode]) -> ListNode:
    # O(n) -> Space
    lAux = []
    # Corner
    if len(lists) == 0:
        return None
    # O(k)
    for i in range(len(lists)):
        # O(n)
        q = parseArray(lists[i])
        if len(q) > 0:
            lAux += q
    if len(lAux) == 0:
        return None
    # O(nlogn)
    lAux.sort()
    # O(n) -> space
    dummy = ListNode(lAux[0])
    res = dummy
    for i in range(1, len(lAux)):
        dummy.next = ListNode(lAux[i])
        dummy = dummy.next
    return res

# O(n)


def parseArray(l: ListNode):
    current = l
    res = []
    while current:
        res.append(current.val)
        current = current.next
    return res


a = ListNode(1, ListNode(3, ListNode(5)))
b = ListNode(2, ListNode(4, ListNode(6)))
print(mergeKLists([a, b]))
