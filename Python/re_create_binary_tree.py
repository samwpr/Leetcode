class Node:
    def __init__(self, input):
        self.root = input
        self.left, self.right = None, None


    def add(self, input):
        if self.root:
            if input <= self.root:
                if self.left == None:
                    self.left = Node(input)
                else:
                    self.left.add(input)
            
            else: 
                if self.right == None:
                    self.right = Node(input)
                else: 
                    self.left.add(input)
        else: 
            self.root = input 

    def inOrder(self, tree):
        res = []
        if tree: 
            res = res + self.inOrder(tree.left)
            res.append(tree.root)
            res = res + self.inOrder(tree.right)
        return res


tree1 = Node(5)
tree1.add(2)
tree1.add(7)

print(tree1.inOrder(tree1))

