class Node:
    def __init__(self, input):
        self.left, self.right = None, None
        self.root = input
    
    def add(self, input):
        if self.root:
            if input < self.root:
                if self.left is None:
                    self.left = Node(input)
                else:
                    self.left.add(self.left)
            else:
                if self.right is None:
                    self.right = Node(input)
                else:
                    self.right.add(self.right)
        else:
            self.root = input

    def inOrder(self, tree):
        res = []
        if tree:
            res = res + self.inOrder(tree.left)
            res.append(tree.root)
            res = res + self.inOrder(tree.right)
        return res 

    def preOrder(self, tree):
        res = []
        if tree: 
            res.append(tree.root)
            res = res + self.preOrder(tree.left)
            res = res + self.preOrder(tree.right)
        return res 

    def postOrder(self, tree):
        res = []
        if tree:
            res = res + self.postOrder(tree.left)
            res = res + self.postOrder(tree.right)
            res.append(tree.root)
        return res 

    def invert(self, tree):
        if not tree:
            return None
        
        temp = tree.left 
        tree.left = tree.right
        tree.right = temp

        self.invert(tree.left)
        self.invert(tree.right)
        return tree


    
tree1 = Node(5)
tree1.add(3)
tree1.add(7)
print(tree1.inOrder(tree1))
#print(tree1.preOrder(tree1))
#print(tree1.postOrder(tree1))
tree1.invert(tree1)
print(tree1.inOrder(tree1))
