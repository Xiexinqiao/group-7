import unittest
from realestate.AVLTree import AVLTree
from realestate.Node import Node
from realestate.Property import Property
from realestate.Client import Client
class TestAVLTree(unittest.TestCase):
    
    def test_left_rotate(self):
        myTree = AVLTree()
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)

        new_root = myTree.leftRotate(root)

        self.assertEqual(myTree.preOrder(new_root), [2, 1, 3])

    def test_right_rotate(self):
        myTree = AVLTree()
        root = Node(3)
        root.left = Node(2)
        root.left.left = Node(1)

        new_root = myTree.rightRotate(root)

        self.assertEqual(myTree.preOrder(new_root), [2, 1, 3])

    def test_get_height(self):
        myTree = AVLTree()
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)

        self.assertEqual(myTree.getHeight(root), 1)

    

    
if __name__ == '__main__':
    unittest.main()
