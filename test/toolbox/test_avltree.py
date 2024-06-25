import unittest
from realestate.toolbox.AVLtree import AVLtree
 
class TestAVLTree(unittest.TestCase):
 
    def setUp(self):
        self.tree = AVLtree()
        print ("he")
    def test_add(self):
        self.assertEqual(self.tree.sum(2, 3), 5)