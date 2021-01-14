class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.insert_helper(self.root, new_val)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)
    
    ####################################    
    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]
    
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
        
    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                if find_val < start.left:
                    return self.preorder_search(start.left, find_val)
                else:
                    return self.preorder_search(start.right, find_val)
        return False
        
    def insert_helper(self, start, new_val):
        if start.value < new_val:
            if start.right:
                self.insert_helper(start.right, new_val)
            else:
                start.right = Node(new_val)
        else:
            if start.left:
                self.insert_helper(start.left, new_val)
            else:
                start.left = Node(new_val)
    ####################################
    
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
