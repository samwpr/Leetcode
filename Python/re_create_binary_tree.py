class Node():
    def __init__(self, input):
        self.left, self.right = None, None
        self.root = input


    def add(self, input):
        if self.root: 
            if input < self.root:
                if self.left is None:
                    self.left = Node(input)
                else:
                    self.left.add(input)
            if input > self.root:
                if self.right is None:
                    self.right = Node(input)
                else:
                    self.right.add(input)
        else:
            self.root = input

    def inOrder(self, tree):
        res = []
        if tree:
            res = res + self.inOrder(tree.left)
            res.append(tree.root)
            res = res + self.inOrder(tree.right)
        return res 

    def diameter(self, tree):
        res = 0










        def dfs(tree):
            nonlocal res

            if not tree:
                return 0
            
        
            
            left = dfs(tree.left)
            print("root A",tree.root)
            print("left: ", left)

            
            right = dfs(tree.right)
            print("root B",tree.root)
            print('right: ', right)

            res = max(res, left + right)
            print('res: ', res)
            

            print("return", 1 + max(left, right))
            print("")

            return 1 + max(left, right)
        
        dfs(tree)
        return res 













tree1 = Node(5)
tree1.add(2)
tree1.add(7)
tree1.add(1)
tree1.add(3)
print(tree1.inOrder(tree1))
tree1.diameter(tree1)