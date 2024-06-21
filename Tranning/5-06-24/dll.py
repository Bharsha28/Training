class Node:
    def __init__(self,n):
        self.data=n
        self.next=None
        self.prev=None
class dll():
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,n):
        if self.head is None:
            self.head=Node(n)
            self.tail=self.head
        else:
            new=Node(n)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def addfront(self,n):
        if self.head is None:
            self.head=Node(n)
            self.tail=self.head
        else:
            new=Node(n)
            temp=self.head
            new.next=self.head
            temp.prev=new
            self.head=new
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
    def search(self,n):
        temp=self.head
        t=self.tail
        f=0
        while(temp!=t and temp.next!=t):
            if temp.data==n or t.data==n :
                    print("elment found")
                    f=1
                    break
            temp=temp.next
            t=t.prev
        if temp.data==n:
            print("Element found")
        if  f==0 :
            print("Eelement not  found")
    def evenodd(self):
        ht=self.head
        tt=self.tail
        c=0
        while(ht!=tt and ht.next!=tt and tt!=None):
            ht=ht.next
            tt=tt.prev
        if ht==tt:
            print("Even lenght")
        else:
              print("odd lenght")
    def palindrome(self):
        t1=self.head
        t2=self.tail
        c=0
        while(t1!=t2 and t1.next!=t2):
            if t1.data==t2.data:
                c=1
            else:
                print("Not palindrome")
                break
            t1=t1.next
            t2=t2.prev
        if c==1:
            print("Plaindrome")
    def rotate(self):
        fast=self.head.next.next
        slow=self.head
        while(fast!=None):
            slow=slow.next
            fast=fast.next.next
        t1=slow.next
        t2=slow
        self.tail.next=self.head
        self.head.prev=self.tail
        self.head=t1
        t2.next=None
        t1.prev=None
    def swap(self):
        temp=self.head.next
        p=self.head
        while(temp!=None):
            n=temp.next
            if p==self.head:
                temp.next=p
                p.prev=temp
                p.next=n
                n.prev=p
                temp.prev=None
                temp=self.head
                prev=self.head
                p=p.next.next
                temp=temp.next.next
            elif temp.next==None :
                temp.prev=p.prev
                temp.next=p
                p.next=None
                p.prev=temp
                break
            else:
                temp.next=p
                temp.prev=p.prev
                p.prev=temp.next.next
                p.next=temp.next
            temp=temp.next
            p=p.next 
obj=dll()
obj.addback(10)
obj.addback(20)
obj.addback(30)
obj.addfront(1)
#obj.addfront(2)
#obj.addfront(3)
#obj.addfront()
obj.display()
print()
#obj.reverse()
obj.search(100)
obj.evenodd()
obj.palindrome()
obj.display()
obj.rotate()
print()
obj.display()
obj.swap()
print()
obj.display()
"""def swap(self):
        temp=self.head.next
        p=self.head
        while(temp!=None):
            n=temp.next
            if p==self.head:
                temp.next=p
                p.prev=temp
                p.next=n
                n.prev=p
                temp.prev=None
                prev=self.head
                p=p.next.next
                temp=temp.next.next
            elif temp.next==None :
                temp.prev=p.prev
                temp.next=p
                p.next=None
                p.prev=temp
                break
            else:
                temp.next=p
                temp.prev=p.prev
                p.prev=temp.next.next
                p.next=temp.next
            temp=temp.next
            p=p.next """