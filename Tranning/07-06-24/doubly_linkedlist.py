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
        while(t!=d and t!=d.next):
            if t.data==key or d.data==key:
                print("found")
                c=1
                break
            else:t=t.next
            d=d.prev
        if t.data==key:
            print("found")
        if c==0:
            print("not found")
    def leo(self):
        t=self.head
        d=self.tail
        while(t!=d and t!=d.next): 
            t=t.next
            d=d.prev
        if t==d:
                print("odd")
        if t==d.next:
                print("even")
    def palin(self):
        t=self.head
        d=self.tail
        f=0
        while(t!=d and t!=d.next):
            if t.data!=d.data:
                print(" not palin")
                f=1
                break
            t=t.next
            d=d.prev
        if f==0:
            print("palin")
    '''def swap(self):
        temp=self.head.next
        p=self.head
        pp=None
        while(temp!=None):
            n=temp.next
            if p==self.head:
                p.next=n
                temp.next=p
                temp.prev=None
                p.prev=temp
                n.prev=p
                p,temp=temp,p
                self.head=temp
            else:
                temp.next=p
                temp.prev=p.prev
                p.prev=temp.next.next
                p.next=temp.next
            temp=temp.next.next
            p=p.next.next'''
    def diff(self,node,es,od):
         if node is None :
             return abs(es-od)
         if node.data%2==0:
             es+=node.data
         elif node.data%2!=0:
             od+=node.data
         t=diff(node.next,es,od)
         return t
    def countprime(self,node,count):
        if node is None:
            return count
        else:
            def prime(i,n,c):
                if i>=n:
                    return c
                if n%i==0:
                        c+=1
                prime(i+1,n,c)
            t=prime(2,node.data,0)
            if t==0:
                k=self.countprime(node.next,count+1)
            else:
                k=self.countprime(node.next,count)
            return k
        
            
l=dll()

head=l.addback(10)
l.addback(2)
l.addback(3)
l.addback(5)
l.addback(40)
#l.addfront(10)
#l.addfront(20)
#l.addfront(30)
l.display()

"""l.search(20)
l.leo()
l.palin()
#l.rotate()
l.display()
print(l.diff(l.head,0,0))"""
print(l.countprime(l.head,0))