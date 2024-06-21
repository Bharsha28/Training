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
    def inorder(self,root):
        if root is None:
              return 
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    def preorder(self,root):
       if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
       if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def sum_all_nodes(self,root):
        if root is None:
            return 0
        return root.data+self.sum_all_nodes(root.left)+self.sum_all_nodes(root.right)
   
    def evendata(self,root):
        if root is None:
            return 0
        if root.data%2==0:
            return root.data+self.evendata(root.left)+self.evendata(root.right)
        else:
            return self.evendata(root.left)+self.evendata(root.right)
        return t
    def odddata(self,root):
        if root is None:
            return 0
        if root.data%2==0:
            return self.odddata(root.left)+self.odddata(root.right)
        else:
            t=root.data+self.odddata(root.left)+self.odddata(root.right)
        return t
    def evenodd(self,root):
        '''if root is None:
            return (e-o)
        if root.data%2==0:
            e=e+root.data+self.evenodd(root.left,e,o)+self.evenodd(root.right,e,o)
        else:
            o=o+root.data+self.evenodd(root.left,e,o)+self.evenodd(root.right,e,o)
        return (e-o)'''
        if root is None:
            return 0
        if root.data%2==0:
            return root.data+self.evenodd(root.left)+self.evenodd(root.right)
        return self.evenodd(root.left)+self.evenodd(root.right)-root.data
    def heigth(self,root):
        if root is None:
            return -1
        left_heigth=self.heigth(root.left)
        rigth_heigth=self.heigth(root.right)
        return max(left_heigth,rigth_heigth)+1
    def balanced(self,root):
        def heigth(self,root):
            if root is None:
                return -1
            left_heigth=self.heigth(root.left)
            rigth_heigth=self.heigth(root.right)
            return max(left_heigth,rigth_heigth)+1
        left=self.heigth(root.left)
        rigth=self.heigth(root.right)
        if abs(left-rigth)<=1:
            return 1
        else:
            return 0
    def countleaf(self,root,c):
        if root is None:
            return 0
        if root.left is None and root.right is None:
          c+=1
        if root.left:
            c=self.countleaf(root.left,c)
        if root.right :
            c=self.countleaf(root.right,c)
        return c
    def countleafsum(self,root,s):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            print("leaf node",root.data)
            s+=root.data
        return s+self.countleafsum(root.left,s)+self.countleafsum(root.right,s)
        #return s
    def search(self,root,tar):
        if root is None:
            return 0
        if root.data==tar:
            return 1
        elif root.data<tar:
            return self.search(root.right,tar)
        else:
            return self.search(root.left,tar)
    def depth(self,root,tar,c):
        if self.search(root,tar):
            if root.data==tar:
                return c
            elif root.data<tar:
                c+=1
                return self.depth(root.right,tar,c)
            else:
                c+=1
                return self.depth(root.left,tar,c)
        else:
            return 0
                
r=Node(5)
r.insert(r,3)
r.insert(r,2)
r.insert(r,4)
r.insert(r,6)
r.insert(r,7)
r.insert(r,8)
r.insert(r,10)
r.inorder(r)
print("\npreorder")
r.preorder(r)
print("\npostorder")
r.postorder(r)
print()
print("sum:",r.sum_all_nodes(r))
print("even sum",r.evendata(r))
print("odd sum:",r.odddata(r))
print("differnece",abs(r.evenodd(r)))
print("heigth",r.heigth(r))
t=r.balanced(r)
if t:
    print("Balanced tree")
else:
    print("Not a Balanced tree")
print("Number of leaf node",r.countleaf(r,0))
print("Number of leaf node",r.countleafsum(r,0))
t=r.search(r,10)
if t:
    print("found")
else:
    print("Not found")
print("depth",r.depth(r,8,0))