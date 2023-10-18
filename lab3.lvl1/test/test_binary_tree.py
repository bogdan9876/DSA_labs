import unittest
from src.binary_tree import BinaryTree, in_order_traversal


class TestInOrderTraversal(unittest.TestCase):
    def test_in_order_traversal(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        result = in_order_traversal(root)
        self.assertEqual(result, [2, 5, 1, 6, 3, 7])


if __name__ == '__main__':
    unittest.main()
