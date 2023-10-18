import unittest
from src.binary_tree import BinaryTree, invert_binary_tree


class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        tree = BinaryTree(3)
        tree.left = BinaryTree(9)
        tree.right = BinaryTree(20)
        inverted_tree = invert_binary_tree(tree)

        self.assertEqual(inverted_tree.value, 3)
        self.assertEqual(inverted_tree.left.value, 20)
        self.assertEqual(inverted_tree.right.value, 9)


if __name__ == '__main__':
    unittest.main()
