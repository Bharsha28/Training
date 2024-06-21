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
    def top(self,root):
        def leftside(root):
            if root is None:
                return
            print(root.data,end=" ")
            return leftside(root.left)
        def rightside(root):
            if root is None:
                return
            print(root.data,end=" ")
            return leftside(root.right)
        leftside(root)
        rightside(root)
    def leftview(self,root):
        def leftside(root):
            if root is None:
                return
            print(root.data,end=" ")
            if root.left==None:
                return leftside(root.right)
            else:
                return leftside(root.left)
        leftside(root)
            
    def rightview(self,root):
        def rightside(root):
            if root is None:
                return
            print(root.data,end=" ")
            if root.right==None:
                return rightside(root.left)
            return rightside(root.right)
        rightside(root)
    def downview(self,root):
        if root is None:
              return 
        if (root.left==None and root.right==None) or  root.left==None or root.right==None:
            print(root.data,end=" ")
#         if (root.left==None and  root.right==None) or 
#             return 
        self.downview(root.left)
        self.downview(root.right)
    def level(root):
        if root is None:
            return
        
        
r=Node(11)
r.insert(r,7)
r.insert(r,5)
r.insert(r,8)
r.insert(r,6)
r.insert(r,10)
#r.insert(r,8)
#r.insert(r,10)
r.top(r)
print("\nleft view:")
r.leftview(r)
print("\nRight  view:")
r.rightview(r)
print("\nDown  view:")
r.downview(r)

