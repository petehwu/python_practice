#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
binary search tree implementation
"""


class Node:

    def __init__(self, data):
        """init method
        """
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        """insert into proper place
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        
    def printTree(self):
        """ prints out the BST
        """
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    
    def lookup(self, lkup):
        """lookup to see if value is in tree
        """
        if self.data > lkup:
            if self.left:
                self.left.lookup(lkup)
            else:
                print("{} not found".format(lkup))
        elif self.data < lkup:
            if self.right:
                self.right.lookup(lkup)
            else:
                print("{} not found".format(lkup))
        else:
            print("{} found".format(self.data))

    def flatten(self, l):
        """flatten BST into an ordered list
        """
        if self.left:
            self.left.flatten(l)
        l.append(self.data)
        if self.right:
            self.right.flatten(l)

    def findSecondLargest(self):
        """ finds the 2nd largest item in the BST
        """
        l = []
        self.flatten(l)
        print(l)
        print(l[-2])


if __name__ == '__main__':
    root = Node(12)
    root.insert(6)
    root.insert(4)
    root.insert(3)
    root.insert(15)
    root.insert(23)
    root.insert(5)
    root.printTree()
    root.lookup(5)
    root.lookup(4)
    root.findSecondLargest()