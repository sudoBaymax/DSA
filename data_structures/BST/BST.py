# Data Structures: Binary Search Tree
# Description: Implementation of a Binary Search Tree
# Author: Joseph Jatou
# Date: 3/12/2025

# There are 4 main operations that can be performed on a BST:
# 1. Insertion
# 2. Deletion
# 3. Traversal (inorder, preorder, postorder)
# 4. Find

# The following is the implementation of a Binary Search Tree

class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

    # insert the value specified in BST
    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = BST(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = BST(val)
            else:
                self.right.insert(val)

    # delete the value specified in BST
    def delete(self, val):
        if val < self.val:
            if self.left is val:
                self.left = None
            else:
                self.left.delete(val)
        elif val > self.val:
            if self.right is val:
                self.right = None

    # Visits the left subtree, then the root, and finally the right subtree.
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.val)
        if self.right:
            self.right.inorder_traversal()

    # Visits the root first, then the left subtree, and finally the right subtree.
    def preorder_traversal(self):
        print(self.val)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    # Visits the left subtree first, then the right subtree, and finally the root.
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.val)

    def find(self, val):
        if val < self.val:
            if self.left is None:
                return False
            else:
                return self.left.find(val)
        if val > self.val:
            if self.right is None:
                return False
            else:
                return self.right.find(val)
        else:
            return True

tree = BST(10)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(22)
tree.insert(11)
tree.insert(12)

