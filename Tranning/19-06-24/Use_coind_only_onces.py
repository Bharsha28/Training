'''finding money can be made from coins in all possible combinations'''
from itertools import combinations
l=[2,3,5,6]
p=[]
k=7
c=0
for i in range(1,len(l)):
    comb=combinations(l,i)
    p.append(list(comb))
print(p)
for i in range(len(p)):
    for j in range(len(p[i])):
        
            if sum(p[i][j])==k:
                c=1
                print(p[i][j])
                break
if c==0:
    print("no")
'''l=[2,3,5,6]
mon=7
c=0
for i in  range(len(l)):
    s=0
    for j in range(i,len(l)):
        s+=l[j]
        if s==mon:
            c=1
            print("yes")
            break
if c==0:
    print("No")
s=0
i=0
j=1
while(i<len(l)):
    s=l[i]
    while(j<len(l)-1):
        s+=l[j]
        print(s,l[j])
        if s==mon:
            c=1
        if s>mon:
            s-=l[j]
            j+=1
    i+=1
    j=i+1
if c==1:
    print("yes")
else:
    print("No")'''
    
        
    