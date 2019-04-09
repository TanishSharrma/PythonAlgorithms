'''

Introduction to Binary Tree and its transversing functions in Python.
Pre-requisites : The person should be well versed in basic Python, OOP and Recursion.
By Tanish Sharrma

'''

class Node:                     # Creating a class Node and defining it's functions
    def __init__(self, data):

        self.left = None        # Left Child of the Node (Empty on creation)
        self.right = None       # Right Child of the Node (Empty on creation)
        self.data = data

    # Insert Node by the method of recursion
    def insert(self, data):

        if self.data:               # To check whether the current Node is empty or not
            if data < self.data:    # If the Node is not empty, then if the data value < Node's Value, we move to its Left Child
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data >= self.data:     # If the data value > Node's Value, we move to its Right Child
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data            # If the node is empty, then we set this as our current Node.

    # Print the Tree (Method used : Recursion)
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

        # Postorder traversal
        # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

        # Preorder traversal
        # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

        # Inorder traversal
        # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # Finding a node by starting at the root node and moving down the tree
    def findNode(self, n):
        root = self
        found = False
        while True:
            if root == None:
                break
            elif root.data == n:
                found = True
                break
            elif root.data > n:
                root = root.left
            else:
                root = root.right
        if found:
            return True
        else:
            return False

# Testing out functions

root = Node(27)     # Creating a new tree by setting the root Node
root.insert(14)     # Inserting Nodes into the tree
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.insert(11)

tran_1 = root.PostorderTraversal(root)   # Post Order Tree Traversal Left ->Right -> Root
tran_2 = root.PreorderTraversal(root)    # Pre Order Tree Traversal Root -> Left -> Right
tran_3 = root.inorderTraversal(root)     # In Order Tree Traversal Left -> Root -> Right

node_exists_1 = root.findNode(42)        # Finding the node with the value 42. Returns True
node_exists_2 = root.findNode(88)        # Finding the node with the value 88. Returns False