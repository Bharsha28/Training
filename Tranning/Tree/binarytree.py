class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.rigth=None
def inorder(root):
        if root is None:
            return
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.rigth)
def preorder(root):
    if root is None:
            return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.rigth)
def postorder(root):
    if root is None:
            return
    postorder(root.left)
    postorder(root.rigth)
    print(root.data,end=" ")
root=Node(4)
root.left=Node(5)
root.rigth=Node(10)
root.left.left=Node(7)
root.left.rigth=Node(8)
root.rigth.rigth=Node(1)
inorder(root)
print()
preorder(root)
print()
postorder(root)