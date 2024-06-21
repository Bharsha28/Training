def diff(node,es,os,d):
         if node is None :
             return t
         if node.data%2==0:
             es+=node.data
         else:
             os+=node.data
         t=diff(node.next,es,os,abs(es-os))
         return t
        
    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

s=list(map(int,input().split()))
head=Node(s[0])
temp=head
pre=None
for i in range(1,len(s)):
    pre=temp
    temp.next=Node(s[i])
    temp=temp.next
    temp.prev=pre
print(diff(head,0,0,0))