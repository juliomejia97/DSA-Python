class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"


def evaluate(root):
    signs = {'*', '/', '+', '-'}
    if not root.val in signs:
        return int(root.val)
    leftVal = evaluate(root.left)
    rightVal = evaluate(root.right)
    if root.val == "*":
        return leftVal*rightVal
    elif root.val == "/":
        return leftVal//rightVal
    elif root.val == "+":
        return leftVal+rightVal
    elif root.val == "-":
        return leftVal-rightVal


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
# 45
