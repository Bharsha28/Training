class node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,v):
        if self.head==None:
            self.head=node(v)
            self.tail=self.head
        else:
            t=node(v)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
    def display(self):
        t=self.head
        while (t!=None):
            print(t.data,end="->")
            t=t.next
        d=self.tail
        print()
        while(d!=self.head):
           print(d.data,end="<-")
           d=d.prev
        print(d.data)
    def balanced(self):
         s=[]
         temp=self.head
         c=0
         while(temp!=None):
             if self.head.data==')' or self.head.data=='}' or self.head.data==']':
                     print(1)
                     break
             else:
                 if temp.data=='(' or temp.data=='{' or temp.data=='[':
                         s.append(temp.data)
                 else:
                     if s and (temp.data==")" and s[-1]=='(') or (temp.data=="}" and s[-1]=='{') or (temp.data=="]" and s[-1]=='['):
                        s.pop()
                 temp=temp.next
             c+=1
         if len(s)==0:
             print(-1)
         else:
            print(c)
            
l=dll()
s=input()
n=len(s)
for i in s:
    l.addback(i)
l.display()
l.balanced()
l.display()
