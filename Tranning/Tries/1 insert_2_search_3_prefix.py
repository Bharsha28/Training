class Node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=Node()
    def insert(self,st):
        temp=self.root
        for i in st:
            if i not in temp.d:
                temp.d[i]=Node()
            temp=temp.d[i]
        temp.flag=1
    def search(self,tar):
        temp=self.root
        c=0
        for i in tar:
            if i in temp.d:
                c+=1
                temp=temp.d[i]
            else:
                print("False")
                break
        if c==len(tar):
            print("True")
    def prefix(self,pre):
        temp=self.root
        c=0
        for i in pre:
            if i in temp.d:
                c+=1
                temp=temp.d[i]
        if c==len(pre):
            print("True")
        else:
            print("False")
    def prefix_count(slef,pre):
        pass
            
obj=tries()
print("Enter no.of strings to insert")
n=int(input())
l=[]
for i in range(n):
    t=int(input())
    y=input()
    l.append((t,y))
q=[]
print(l)

for i in range(len(l)):
    if l[i][0]==1:
        obj.insert(l[i][1])        
    if l[i][0]==2:
        obj.search(l[i][1])           
    if l[i][0]==3:
        obj.prefix(l[i][1])
'''4
word
words
world
wood'''
    
