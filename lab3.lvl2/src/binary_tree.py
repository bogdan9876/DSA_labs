
class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree) -> BinaryTree:
    if tree is None:
        return tree

    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)
    tree.left, tree.right = tree.right, tree.left

    return tree

