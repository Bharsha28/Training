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
        if root is None:
            return
        queue=[(root,0)]
        c=0
        d={}
        while queue:
            m=queue.pop(0)
            ele=m[0]
            c=m[1]
            if c not in d.keys():
                d[c]=ele.data
            if ele.left:
                queue.append((ele.left,c-1))
            if ele.right:
                queue.append((ele.right,c+1))
        return d
    def leftview(self,root,q,c):
        if root is None:
            return
        if c not in q:
            print(root.data,end=" ")
        q.append(c)
        self.leftview(root.left,q,c+1)
        self.leftview(root.right,q,c+1)
    def rightview(self,root,q,c):
        if root is None:
            return
        if c not in q:
            #print(c,end=" ")
            print(root.data,end=" ")
        q.append(c)
        self.rightview(root.right,q,c+1)
        self.rightview(root.left,q,c+1)
    def downview(self,root):
        if root is None:
            return
        queue=[(root,0)]
        c=0
        d={}
        while queue:
            m=queue.pop(0)
            ele=m[0]
            c=m[1]
            if c not in d.keys():
                d[c]=[]
                d[c].append(ele.data)
            else:
                d[c].append(ele.data)
            #print(d)
            if ele.left:
                queue.append((ele.left,c-1))
            if ele.right:
                queue.append((ele.right,c+1))
        return d
        
r=Node(10)
r.insert(r,15)
r.insert(r,5)
r.insert(r,2)
r.insert(r,7)
r.insert(r,11)
r.insert(r,8)
r.insert(r,9)
#r.insert(r,3)
#r.insert(r,14)
#r.insert(r,13)
print("top view:")
d=r.top(r)
#print(d)
for i in sorted(d):
    print(d[i],end=" ")
print("\nleft view:")
r.leftview(r,[],0)
print("\nRight  view:")
r.rightview(r,[],0)
print("\nDown  view:")
d=r.downview(r)
#print(d)
for i in d.values():
    print(i[-1],end=" ")
