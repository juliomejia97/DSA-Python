class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k, floor=None, ceil=None):
    # Fill this in.
    return [findFloor(root_node, k), findCeil(root_node, k)]


def findFloor(root_node, k):
    if(root_node.left == None and root_node.right == None):
        if root_node.value < k:
            return root_node.value
        else:
            return -1
    if root_node.value == k:
        return root_node.value
    if root_node.value > k:
        left = findFloor(root_node.left, k)
        if root_node.value <= k and left <= k:
            return left if abs(left-k) < abs(root_node.value-k) else root_node.value
        elif left <= k:
            return left
    val = findFloor(root_node.right, k)
    return val


def findCeil(root_node, k):
    # Base Case - Leaft Node
    if(root_node.left == None and root_node.right == None):
        if root_node.value > k:
            return root_node.value
        else:
            return -1
    if root_node.value == k:
        return root_node.value
    if root_node.value > k:
        left = findCeil(root_node.left, k)
        if root_node.value >= k and left >= k:
            return left if abs(left-k) < abs(root_node.value-k) else root_node.value
        elif root_node.value >= k:
            return root_node.value
    val = findCeil(root_node.right, k)
    return val


root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)
