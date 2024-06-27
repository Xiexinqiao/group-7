import unittest
from realestate.AVLTree import AVLTree
from realestate.Node import Node
from realestate.Property import Property
from realestate.Client import Client
class TestAVLTree(unittest.TestCase):
        def test_Property_class(self):
            prop = Property(1, "1234 Elm St", 300000, "HOUSE", "AVAILABLE")
            self.assertEqual(str(prop), "Property ID: 1, Address: 1234 Elm St, Price: $300000, Type: HOUSE, Status: AVAILABLE, Owner: None")
