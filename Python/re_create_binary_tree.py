class Node: 
    def __init__(self, input):
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


    def inOrder(self, root):
        res =[]
        if root:
            res = res + self.inOrder(root.left)
            res.append(root.root)
            res = res + self.inOrder(root.right)
        return res 

    def preOrder(self, root):
        res = []
        if root:
            res.append(root.root)
            res = res + self.preOrder(root.left)
            res = res + self.preOrder(root.right)
        return res 

    def postOrder(self, root):
        res = []
        if root: 
            res = res + self.postOrder(root.left)
            res = res + self.postOrder(root.right)
            res.append(root.root)
        return res 

def invert(root):
    if not root:
        return None
    
    temp = root.left 
    root.left = root.right
    root.right = temp 

    invert(root.left)
    invert(root.right)
    return root
            


    
tree1 = Node(5)
tree1.printRoot()
tree1.insert(3)
tree1.insert(7)
print(tree1.inOrder(tree1))
tree1 = invert(tree1)
print(tree1.inOrder(tree1))
#print(tree1.preOrder(tree1))
#print(tree1.postOrder(tree1))


