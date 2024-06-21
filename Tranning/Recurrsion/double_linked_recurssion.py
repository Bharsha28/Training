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
    def display(self,node):
        if node is None:
            return 
        print(node.data,end=" ")
        return self.display(node.next)
    '''def search(self,node,tail,key):
        if tail.next==node:
            return 0
        if node.next==tail:
            return 0
        if node.data==key or tail.data==key:
            return 1
        return self.search(node.next,tail.prev,key)
    def evenoddnum(self,node,e,o):
        if node is None:
            return e,o
        if node.data%2==0:
            e.append(node.data)
        else:
            o.append(node.data)
        return self.evenoddnum(node.next,e,o)
    def lengthevenodd(self,fast,slow):
        if fast==None:
            return 'e'
        elif fast.next==None:
            return 'o'
        return self.lengthevenodd(fast.next.next,slow.next)
    def palin(self,node,tail):
        if node.next==tail or node==tail:
            return 1
        if node.data==tail.data:
            return self.palin(node.next,tail.prev)
        return 0
    def diffevenoddsum(self,node,esum,osum):
        if node is None:
           return abs(esum-osum)
        if node.data%2==0:
            esum+=node.data
        else:
            osum+=node.data
        return self.diffevenoddsum(node.next,esum,osum)
    def countprime(self,node,count):
        if node is None:
            return count
        def prime(val,i):
            if val==1:
                return 1
            if i==((val)//2)+1:
                return 0
            elif val%i==0:
                return 1
            else:
                return 0
            return prime(val,i+1)
        t=prime(node.data,2)
        if t==0:
           # print(node.data,count)
            count+=1
        return self.countprime(node.next,count)'''
    def validparanthesis(self,node,s,c):
        if node is None :
            if not s:
                return [1,c]
            else:
                return [0,c+1]
        else:
                 if node.data=='(' or node.data=='{' or node.data=='[':
                         s.append(node.data)
                 else:
                     if s and (node.data==")" and s[-1]=='(') or (node.data=="}" and s[-1]=='{') or (node.data=="]" and s[-1]=='['):
                        s.pop()
                 return self.validparanthesis(node.next,s,c)
                 c+=1            
l=dll()
head=l.addback('(')
l.addback(')')
l.addback('{')
l.addback('}')
l.addback('[')
tail=l.addback('[')
l.display(l.head)
print()
#print(l.display(l.head))
'''if l.search(l.head,l.tail,3):
    print("found")
else:
    print("Not found")
print(l.evenoddnum(l.head,[],[]))
res=l.lengthevenodd(l.head,l.head)
if res=='e':
    print("even length")
else:
    print("odd lenght")
res=l.palin(l.head,l.tail)
if res:
    print("Palindrome")
else:print("Not palindrome")
print(l.diffevenoddsum(l.head,0,0))
print(l.countprime(l.head,0))'''
if l.head.data==')' or l.head.data=='}' or l.head.data==']':
    print("Not balance")
else:
    t=l.validparanthesis(l.head,[],0)
    if t[0]==1:
        print("Balanced")
    else:
        print("not balanced",t[1])
