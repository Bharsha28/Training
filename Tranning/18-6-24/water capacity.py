l=[2,5,2,3,6,7,1,0,5,7]
L=0
R=2
c=0
while(R<len(l)):
   i=R-1
   if l[L]>l[i] and l[i]<l[R]:
       c+=abs(l[L]-l[R-1])
   else:
         if l[L]>l[i] and l[i]<L[R]:
             c+=abs(l[L]-l[i])
             i+=1
         i+=1
         R+=1
   L+=1
   R+=2
print(c)
l1=[0]*len(l)
l2=[]
max1=max(l)
l2=[max1]*len(l)
print(l2)
m1=0
for i in range(len(l)):
    if l[i]>m1:
        m1=l[i]
    l1[i]=m1
print(l1)
c=0
for i in range(len(l)):
    min1=min(l1[i],l2[i])
    c+=abs(min1-l[i])
print(c)

            