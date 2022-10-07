class Node: 
    def __init__(self, input = None):
        self.left = None 
        self.right = None
        self.root = input

    def printRoot(self):
        print(self.root)

    def insert(self, input):
        if self.root:
            if input < self.root:
                if self.left is None:
                    self.left = Node(input)
                else: 
                    self.left.insert(input)
            else:
                if self.right is None:
                    self.right = Node(input)
                else:
                    self.right.insert(input)
        else: 
            self.root = input

    def inOrder(self, treeRoot):
        res = []
        if treeRoot:
            res = res + self.inOrder(treeRoot.left)
            res.append(treeRoot.root)
            res = res + self.inOrder(treeRoot.right)
        return res 

    def preOrder(self, treeRoot):
        res = []
        if treeRoot:
            res.append(treeRoot.root)
            res = res + self.preOrder(treeRoot.left)
            res = res + self.preOrder(treeRoot.right)
        return res

    def postOrder(self, treeRoot):
        res = []
        if treeRoot:
            res = res + self.postOrder(treeRoot.left)
            res = res + self.postOrder(treeRoot.right)
            res.append(treeRoot.root)
        return res 

        
def invert(tree):
    if not tree:
        return None 

    temp = tree.left 
    tree.left = tree.right
    tree.right = temp 

    invert(tree.left)
    invert(tree.right)
    return tree





        

tree1 = Node(5)
tree1.insert(3)
tree1.insert(2)
tree1.insert(4)
tree1.insert(7)
tree1.insert(6)
tree1.insert(8)
print(tree1.left.root)
print(tree1.right.root)
print(tree1.left.left.root)

print(tree1.preOrder(tree1))
print(tree1.postOrder(tree1))

print(tree1.inOrder(tree1))
invert(tree1)
print(tree1.inOrder(tree1))



'''
In order = left, root, right 
Pre Order = root, left, right 
Post Order = left, right, root 
'''
    
        

