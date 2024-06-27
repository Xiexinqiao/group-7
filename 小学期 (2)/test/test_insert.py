import unittest
from realestate.AVLTree import AVLTree
from realestate.Node import Node
from realestate.Property import Property
from realestate.Client import Client
class TestAVLTree(unittest.TestCase):
    
    
    
    def test_insert(self):
        # 创建 AVL 树实例
        myTree = AVLTree()

        # 插入节点
        root = None
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            root = myTree.insert(root, key)

        # 验证前序遍历结果
        self.assertEqual(myTree.preOrder(root), [30, 20, 10, 25, 40, 50])

        # 验证平衡因子
        self.assertEqual(myTree.getBalance(root), 0)
        self.assertEqual(myTree.getBalance(root.left), 0)
        self.assertEqual(myTree.getBalance(root.right), -1)
        self.assertEqual(myTree.getBalance(root.left.left), 0)
        self.assertEqual(myTree.getBalance(root.left.right), 0)
        self.assertEqual(myTree.getBalance(root.right.left), 0)
        self.assertEqual(myTree.getBalance(root.right.right), 0)

        # 验证高度
        self.assertEqual(myTree.getHeight(root), 3)
        self.assertEqual(myTree.getHeight(root.left), 2)
        self.assertEqual(myTree.getHeight(root.right), 2)
        self.assertEqual(myTree.getHeight(root.left.left), 1)
        self.assertEqual(myTree.getHeight(root.left.right), 1)
        self.assertEqual(myTree.getHeight(root.right.left), 0)
        self.assertEqual(myTree.getHeight(root.right.right), 1)