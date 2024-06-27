class Property:
    def __init__(self, property_id, address, price, property_type, status, owner=None):
        self.property_id = property_id
        self.address = address
        self.price = price
        self.property_type = property_type
        self.status = status
        self.owner = owner  
  
    def preOrder(self, root):  
        if root is None:  
            return []  
        result = [root.property_id]   
        result.extend(self.preOrder(root.left))  
        result.extend(self.preOrder(root.right))  
        return result 
    def __str__(self):
        return (f"Property ID: {self.property_id}, Address: {self.address}, "
                f"Price: ${self.price}, Type: {self.property_type}, "
                f"Status: {self.status}, Owner: {self.owner.name if self.owner else 'None'}")
    
    def __lt__(self, other):  
        if isinstance(other, Property):  
            return self.price < other.price  
        return NotImplemented