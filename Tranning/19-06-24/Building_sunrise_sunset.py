#l=[3,5,9,6,8,10]
l=[3,4,5,10,4,3]
cr=0
cs=0
l1=set()
l2=set()
for i in range(len(l)):
    if l[i]>cr:
        cr=l[i]
    l1.add(cr)
print(l1)
for i in range(len(l)-1,-1,-1):
    if l[i]>cs:
        cs=l[i]
    l2.add(cs)
print(l2)