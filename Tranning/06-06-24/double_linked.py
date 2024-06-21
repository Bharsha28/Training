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
            print(t.data,end=" ")
            t=t.next
        d=self.tail
        print()
        while(d!=self.head):
           print(d.data,end=" ")
           d=d.prev
        print(d.data)
    def addfront(self,v):
        if self.head==None:
            self.head=node(v)
            self.tail=self.head
        else:
            t=node(v)
            d=self.head
            t.next=d  
            d.prev=t
            self.head=t
    def search(self,key):
        t=self.head
        d=self.tail
        c=0
        while(t!=None and d!=None and t.next!=d):
            if t.data==key or d.data==key:
                print("found")
                c=1
                break
            else:t=t.next
            d=d.prev
        if c==0:
            print("not found")
             
l=dll()
l.addback(1)
l.addback(2)
l.addback(3)
l.addback(4)
l.display()
l.addfront(10)
l.addfront(20)
l.addfront(30)
l.display()

l.search(200)