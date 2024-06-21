class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
    def insert(self,root,key):
        if root is None:
            return Node(key)
        else:
            if root.data==key:
                return root
            elif root.data<key:
                root.right=self.insert(root.right,key)
            else:
                root.left=self.insert(root.left,key)
        return root
    def search(self,root,key):
        if root is None:
            return root
        if root.data==key:
            return 1
        elif root.data<key:
            return self.search(root.right,key)
        else:
            return self.search(root.left,key)
def countleaf(root,c):
        if root is None:
            return c
        if root.left is None and root.right is None:
            c += 1
        if root.left is not None:
            c=countleaf(root.left,c)
        if root.right is not None:
            c=countleaf(root.right,c)
        return c
def evensumdiff(root):
        if root is None:
            return 0
        if root.data%2==0:
            s+=root.data
            s=s+evensumdiff(root.left)+evensumdiff(root.right)
        else:
           root.data+evensumdiff(root.left)+evensumdiff(root.right)
        return 
        
def inorder(root):
      if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
r=Node(7)
r.insert(r,10)
r.insert(r,15)
r.insert(r,5)
r.insert(r,2)
r.insert(r,1)
r.insert(r,3)
#r.insert(r,90)
inorder(r)
print()
t=r.search(r,90)
if t==1:
    print("found")
else:
    print("not found")
print(countleaf(r,0))
print(evensumdiff(r))
''''''