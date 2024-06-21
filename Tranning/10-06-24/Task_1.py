'''ip:[2,3,1,3,4,3,2]
op:[[2,3,1,4].[3,2],[3]]'''
l=list(map(int,input().split()))
l1=[]
'''c=0
while(c!=len(l)):
    l2=[]
    for i in range(len(l)):
        if l[i]!='0':
            if l[i] not in l2:
                c+=1
                l2.append(l[i])
                l[i]='0'
    l1.append(l2)
   if l.count('0')==len(l):
        break
print(l1)'''
d={}
c=0
for i in l:
    if i not in d:
        d[i]=i
    else:
        d[i]+=1
while(c!=len(l)):
    l2=[]
    for i in d:
        if d[i]!=0:
            c+=1
            l2.append(i)
            d[i]=d[i]-1
print(l1)
   
