from typing import List


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def in_order_traversal(root: BinaryTree) -> List:
    if not root:
        return []
    result = []
    if root.left:
        result += in_order_traversal(root.left)
    result.append(root.value)
    if root.right:
        result += in_order_traversal(root.right)
    return result
