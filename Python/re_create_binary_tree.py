#Try this to visualize binary tree: https://www.geeksforgeeks.org/binarytree-module-in-python/

'''
In-Order - Root in the middle 
left -> subtree -> root -> right -> subtree

Pre-Order - Root at the start 
root -> left -> subtree -> right -> subtree

Post-Order - Root at the end 
left -> subtree -> right -> subtree -> root

Left will always come before right, when the root will be visited that is different 
'''  

class Node:
    def __init__(self, input):
        self.left = None 
        self.right = None 
        self.data = input 

    def printRoot(self):
        print(self.data)

    def insert(self, input):
        if self.data:
            if input < self.data:
                if self.left is None: 
                    self.left = Node(input)
                else: 
                    self.left.insert(input)
            else:
                input > self.data
                if self.right is None:
                    self.right = Node(input)
                else: 
                    self.right.insert(input)
        else:
            self.data = input

    def InOrder(self, root): 
        result = []
        if root:
            result = self.InOrder(root.left)
            result.append(root.data)
            result = result + self.InOrder(root.right)
        return result


    def PreOrder(self, root):
        result = []
        if root: 
            result.append(root.data)
            result = result + self.PreOrder(root.left)
            result = result + self.PreOrder(root.right)
        return result

    def PostOrder(self, root):
        result = []
        if root: 
            result = result + self.PostOrder(root.left)
            result = result + self.PostOrder(root.right)
            result.append(root.data)
        return result

def InvertTree(root):
    if not root:
        return None

    temp = root.left 
    root.left = root.right 
    root.right = temp 

    InvertTree(root.left)
    InvertTree(root.right)
    return root

def PrintInOrder(root):
    if not root:
        return None

    PrintInOrder(root.left)
    print(root.data, end=' ')
    PrintInOrder(root.right)


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print("In Order",root.InOrder(root))
print("Pre Order",root.PreOrder(root))
print("Post Order",root.PostOrder(root))
print("")
PrintInOrder(root)
InvertTree(root)
print("")
PrintInOrder(root)



    




    