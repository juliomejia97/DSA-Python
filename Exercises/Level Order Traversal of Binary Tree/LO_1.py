class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelOrder(self, root):
        if not root:
            return []
        levels = self.countLevels(root)
        res = [[]] * levels
        self.levelOrder_Aux(root, res, 0)
        return res

    def countLevels(self, root):
        if not root:
            return 0
        left = 1 + self.countLevels(root.left)
        right = 1 + self.countLevels(root.right)
        return max(left, right)

    def levelOrder_Aux(self, root, res, level: int):
        res[level] = res[level]+[root.val]
        if root.left:
            self.levelOrder_Aux(root.left, res, level+1)
        if root.right:
            self.levelOrder_Aux(root.right, res, level+1)


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print(root.levelOrder(root))
# 1 2 3 4 5
