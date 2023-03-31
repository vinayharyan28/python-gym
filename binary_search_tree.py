class BSTNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is None:
            self.val = val
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


    def delete(self, val):
        if self.val is None:
            return
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        
        if self.right is None:
            return self.left
        
        if self.left is None:
            return self.right
        
        min_max = self.right
        while min_max.left:
            min_max = min_max.left
        self.val = min_max.val
        self.right = self.right.delete(val)
        return self
    
    def get_min(self):
        min_val = self
        while min_val.left:
            min_val = min_val.left
        return min_val.val
    
    def get_max(self):
        max_val = self
        while max_val.right:
            max_val = max_val.right
        return max_val.val
    
    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals
    
    def search(self, val):
        if self.val == val:
            return True
        if val < self.val:
            if self.left is None:
                return False
            return self.left.search(val)
        
        if self.right is None:
            return False
        return self.right.search(val)

        
        
    
if __name__ == '__main__':
    bst = BSTNode()
    bst.insert(44)
    bst.insert(88)
    bst.insert(17)
    bst.insert(8)
    bst.insert(32)
    bst.insert(28)
    bst.insert(29)
    bst.insert(65)
    bst.insert(97)
    bst.insert(54)
    bst.insert(82)
    bst.insert(93)
    bst.insert(76)
    bst.insert(80)
    bst.delete(32)
    print(bst.search(32))
    print(bst.get_min())
    print(bst.get_max())
    print(bst.inorder([]))