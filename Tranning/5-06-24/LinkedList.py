class Node:
    def __init__(self,n):
        self.data=n
        self.next=None
class sll():
    def __init__(self):
        self.head=None
    def addback(self,n):
        if self.head is None:
            self.head=Node(n)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=Node(n)
    def addfront(self,n):
        if self.head is None:
            self.head=Node(n)
        else:
            temp=self.head
            new=Node(n)
            new.next=temp
            self.head=new
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
    def position(self,n,pos):
        temp=self.head
        c=1
        while(temp.next!=None and c!=pos-1):
            temp=temp.next
            c+=1
        new=Node(n)
        new.next=temp.next
        temp.next=new
    def search(self,n):
        temp=self.head
        c=0
        while(temp!=None):
            if temp.data==n:
                c=1
            temp=temp.next
        if c==0:
            print("Not found")
        else:
            print("found")
    def middleele(self):
        temp=self.head
        slow=temp
        fast=temp
        while(fast!=None and fast.next!=None):
                slow=slow.next
                fast=fast.next.next
        print("Middle element",slow.data)
    def length(self):
        temp=self.head
        slow=temp
        fast=temp
        l=1
        while(fast!=None and fast.next!=None):
                    slow=slow.next
                    l+=2
                    fast=fast.next.next
        if l%2!=0:
            print("even length")
        else:
            print("odd length")
        print("length of linkedlist",l)
        #or
        if fast==None:
            print("even length")
        else:
            print("odd length")
    def long(self):
            temp=self.head
            tempn=self.head.next
            c=1
            max1=0
            val=temp.data
            while(tempn!=None):
                val=temp.data+1
                if tempn.data==val:
                    c+=1
                    val=tempn.data
                else:
                    c=1
                    val=temp.data
                temp=temp.next
                tempn=tempn.next
                max1=max(max1,c)
            print("longest sub lenght",max1)
    def bubblesort(self):
        temp=self.head
        p=None
        c=0
        while(temp!=None):
            t=self.head
            f=0
            while(t.next!=p):
                if t.data>t.next.data:
                    f=1
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
                c+=1
            if f==0:
                break
            p=t
            temp=temp.next
        print("iteration",c)
    def pair(self):
        tempnxt=self.head
        temp=None
        while(tempnxt!=None):
            temp=tempnxt.next
            while(temp!=None):
                    print("pairs are",str(tempnxt.data)+str(temp.data))
                    temp=temp.next
            tempnxt=tempnxt.next
    def reverse(self):
        temp=self.head
        prev=None
        next=None
        
        
obj=sll()
obj.head=Node(1)
obj.addback(2)
obj.addback(3)
obj.addback(9)
obj.addback(1)
obj.addback(6)
obj.addback(7)
obj.display()
print()
#obj.addfront(5)
obj.display()
obj.position(5,4)
print("\ninserting at position")
obj.display()
print("searching an element in the linkedlist")
obj.search(100)
obj.middleele()
obj.length()
obj.long()
obj.bubblesort()
print("sorted:")
obj.display()
print()
obj.pair()
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("->",end=" ")
                temp=temp.next
                if temp==self.head:
                    break
    def detectCycle(self, head):
        d={}
        temp=head
        c=0
        while(temp!=None):
            if temp.data not in d:
                d[temp.data]=c
            else:
                return  d[temp.data]
                break
            c+=1
            temp=temp.next
        return -1
                
obj=singlell()
n=node(10)
obj.head=n
n1=node(20)
n.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
n5=node(60)
n4.next=n5
n5.next=n1
#obj.display()
print("loop found at :")
print(obj.detectCycle(n))'slow=head
        fast=head
        c=0
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                slow=head
                c=0
                while(slow!=fast):
                    slow=slow.next
                    fast=fast.next
                    c+=1
            c+=1
        if c==0:
            return -1
        else:
            return c'''

