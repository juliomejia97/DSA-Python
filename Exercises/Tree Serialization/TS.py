from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # pre-order printing of the tree.
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


def serialize(root: Node) -> str:
    if not root:
        return "#"
    leftSubTree = serialize(root.left)
    rightSubTree = serialize(root.right)

    return "".join(str(root.val)+" "+leftSubTree+" "+rightSubTree)

#1 3 2 # # 5 # # 4 # 7 # #


def deserialize(data: str) -> Node:
    q = deque(data.split(' '))
    return deserialize_helper(q)
    #     1
    #    / \
    #   3   4
    #  / \   \
    # 2   5   7


def deserialize_helper(q: deque) -> Node:
    val = q.popleft()
    if val == '#':
        return None
    else:
        newNode = Node(int(val))
        newNode.left = deserialize_helper(q)
        newNode.right = deserialize_helper(q)
        return newNode


tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

serializedTree = serialize(tree)
# 1 3 2 # # 5 # # 4 # 7 # #
print(deserialize(serializedTree))
# 132547
