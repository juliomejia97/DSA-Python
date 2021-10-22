from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelOrder(self, root):
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            current_level = []
            for _ in range(len(q)):
                node = q.popleft()
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(current_level)
        return res


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print(root.levelOrder(root))
# 1 2 3 4 5
